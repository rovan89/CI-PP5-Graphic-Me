from decimal import Decimal
from django.conf import settings
from products.models import Category
from shop.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def bag_contents(request):

    """
    This function calculates the users order,
    including a discount if the user reaches a certain threshold
    """

    bag_items = []
    ordered_items = []
    total = 0
    is_paid = None
    cart_total = 0
    discount = 0
    product_count = 0
    grand_total = 0
    category_price = 0
    category_name = None
    concept_price = 0
    category = Category.objects.all().values()

    if request.user.is_authenticated:
        order_item = Order.objects.filter(user=request.user)
        category = Category.objects.all().values()
        current_user = request.user.id
        order_user_id = None

        for ordered_item in order_item:
            order_user_id = ordered_item.user_id
            ordered_category_id = ordered_item.user_id
            category_name = str(ordered_item.category)
            is_paid = ordered_item.paid
            date = ordered_item.date

            for i in category:
                cat_name = i.get('friendly_name')
                if cat_name == category_name:
                    category_price = i.get('price')

            if current_user == order_user_id and ordered_item.paid is not True:
                concept_bag = ordered_item.number_of_concepts
                concept_price = 100 * concept_bag
                total = concept_price + category_price

                ordered_items.append({
                    'ordered_item': ordered_item,
                    'concept_price': concept_price,
                    'category_price': category_price,
                    'category_name': category_name,
                    'date': date,
                    'is_paid': is_paid,
                    'total': total,
                })

                bag_items.append({
                    'ordered_item': ordered_item,
                    'concept_price': concept_price,
                    'category_price': category_price,
                    'category_name': category_name,
                    'is_paid': is_paid,
                    'total': total,
                })

        for i in bag_items:
            sub_total = i.get('total')

            if current_user == order_user_id:
                cart_total = cart_total + sub_total

        if cart_total > settings.DISCOUNT_THRESHOLD:
            discount = cart_total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
            grand_total = cart_total - discount
        else:
            grand_total = cart_total

        context = {
            'order_item': order_item,
            'bag_items': bag_items,
            'ordered_items': ordered_items,
            'category_name': category_name,
            'category_price': category_price,
            'total': cart_total,
            'is_paid': is_paid,
            'product_count': product_count,
            'discount': discount,
            'grand_total': grand_total,

        }

        return context

    else:

        return ordered_items
