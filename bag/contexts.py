from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total > settings.DISCOUNT_THESHOLD:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
    else:
        discount = 0

    grand_total = discount + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'grand_total': grand_total,
    }

    return context
