from decimal import Decimal
from django.conf import settings
from products.models import Category

def bag_contents(request):

    """ 
    This function calculates the users order,
    including a discount if the user reaches a certain threshold
    
     """

    bag_items = []
    total = 0
    category_price = 0
    category_name = None
    concept_price = 100
    bag = request.session.get('bag', {})
    
    for item in bag.items():
        category_item = Category.objects.all().values()
        if 'category' in item:
            item = int(item[1])
            for i in category_item:
                if(item == i['id']):
                    print('Success: ', item, '==', i)
                    category_price = i['price']
                    category_name = i['name']
                    concept_bag = int(bag['number_of_concepts'])
                    concept_price = concept_price * concept_bag

    total = concept_price + category_price

    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        grand_total = total - discount
    else:
        total = 0

    bag_items.append({
        'bag': bag,
        'concept_price': concept_price,
        'category_price': category_price,
        'category_name': category_name,
        'total': total,
        
    })


    context = {
        'bag_items': bag_items,
        'total': total,
        'discount': discount,
        'grand_total': grand_total,

    }

    return context
