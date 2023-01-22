import uuid
import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from shop.models import Order
from shop.forms import OrderForm
from bag.contexts import bag_contents

@login_required
def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')

@login_required
def add_to_bag(request):

    # print("|| bag/views.py || ITEM DICT = ", request.POST.dict())

    bag = request.session.get('bag', {})
    user_order = dict(request.POST.items())
    # print("|| bag/views.py || BAG: ", bag)
        
    bag = user_order
    request.session['bag'] = bag
    return redirect("home")

@login_required
def remove_from_bag(request, ordered_item):
    # print("\n|| bag/views.py || _______________________________________________")
    in_bag_order_item = Order.objects.filter(user=request.user)
    # print("|| bag/views.py || All ORDERED ITEMS = ", in_bag_order_item, type(in_bag_order_item))

    # print("|| bag/views.py || ORDERED ITEM: ", ordered_item, type(ordered_item))
    try:
        for i in in_bag_order_item:
            item = str(i)
            print("|| bag/views.py || ORDER ITEM I: ", i, type(i))
            if item == ordered_item:
            # order_number = in_bag_order_item.get('order_number')
                # print("|| bag/views.py || ORDER ITEM I = ", item, type(item))
                # print("|| bag/views.py || ORDER NUMBER = ", order_number, type(order_number))

                i.delete()
                print("|| bag/views.py || WORKING")
                return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


@login_required
def edit_item(request, item_id):
    order = get_object_or_404(Order, id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_bag')
    form = OrderForm(instance=order)

   
    print("|| bag/views.py || EDIT ITEM: ", request)
    print("|| bag/views.py || EDIT ITEM: ", request)

    context = {
        'form': form
    }

    return render(request, 'bag/edit_item.html', context)


    # bag = request.session.get('bag', {})
    # user_order = dict(request.POST.items())
    # print("|| bag/views.py || BAG: ", bag)
    # print("|| bag/views.py || USER ORDER: ", user_order)
  

    print("|| bag/views.py || _______________________________________________")

    return redirect(reverse('view_bag'))

def chekout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order_number = request.POST.get('order_number')
    category = request.POST.get('category')
    price = request.POST.get('grand_total')

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    print("|| bag/views.py || TOTAL: ", total, type(total))


    stripe_total = round(total * 100)
    print("|| bag/views.py || STRIPE TOTAL: ", stripe_total, type(stripe_total))
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        message.warning(request, 'Stripe public key is missing. \
             Did you forget to set it in your enviroment?')
    

    context = {
        'order_number': order_number,
        'category': category,
        'price': price,
        'stripe_public_key': stripe_public_key,
        'clent_secret': intent.client_secret,
    }

    return render(request, 'bag/checkout.html', context)