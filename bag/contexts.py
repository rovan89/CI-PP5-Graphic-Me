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
    cart_total = 0
    discount = 0
    product_count = 0
    grand_total = 0
    category_price = 0
    category_name = None
    cat_id = 0
    concept_price = 0
    bag = request.session.get('bag', {})
    
    if request.user.is_authenticated:
        # print(bag)
        order_item = Order.objects.filter(user=request.user)
        # print(order_item)
        # print("| contexts.py | ORDER ITEM: ", order_item)
                    

        category = Category.objects.all().values()
        current_user = request.user.id

        order_user_id = None

            
        for ordered_item in order_item:
            # print(type(ordered_item))
            order_user_id = ordered_item.user_id
            # print("\n| contexts.py | ORDER_USER_ID: ", order_user_id)
            # print("\n| contexts.py | ORDER_USER_ID: ", order_user_id)

            ordered_category_id = ordered_item.user_id
            # print("CATEGORY ORDER ID: ",  ordered_category_id)
            for i in category:
                cat_id = i.get('id')
                cat_name = i.get('friendly_name')
                if cat_id == ordered_category_id:
                    category_name = cat_name
                    category_price = i.get('price')
                    
            if current_user == order_user_id:
                concept_bag = ordered_item.number_of_concepts
                concept_price = 100 * concept_bag

                total = concept_price + category_price
                
                ordered_items.append({
                    'ordered_item': ordered_item,
                    'concept_price': concept_price,
                    'category_price': category_price,
                    'category_name': category_name,
                    'total': total,
                }) 

                bag_items.append({
                    'ordered_item': ordered_item,
                    'concept_price': concept_price,
                    'category_price': category_price,
                    'category_name': category_name,
                    'total': total,
                })
        
        
    
            # print("\n| contexts.py | BAG ITEMS: ", bag_items)
            
        for i in bag_items:
            # print("\n| contexts.py | ORDER USER I: ", i.get('total'))
            # print("\n| contexts.py | BAG ITEMS I: ", i)
            sub_total = i.get('total')
            if current_user == order_user_id:
                cart_total = cart_total + sub_total
                # print("\n| contexts.py | ORDER USER FOR LOOP: ", cart_total)


            #for i in order_user:
                #    for x in order_item:
                #        i = str(i)
                #        x = x.get("order_number")
                #        x = str(x)
                #       print("\n| contexts.py | ORDER USER FOR LOOP: ", i, type(i))
                #       print("| contexts.py | ORDER_ITEM USER FOR: ", x, type(x))
                #       print("_________________________________________________________________________")
                #       if x == i:
                #           print("WORKING")
                            

        if cart_total > settings.DISCOUNT_THRESHOLD:
            discount = cart_total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
            grand_total = cart_total - discount
        else:
            grand_total = cart_total

        context = {
            'bag_items': bag_items,
            'ordered_items': ordered_items,
            'category_price': category_price,
            'total': cart_total,
            'product_count': product_count,
            'discount': discount,
            'grand_total': grand_total,

        }

        return context
    
    else:
        
        return ordered_items

