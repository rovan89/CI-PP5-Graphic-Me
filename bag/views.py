import uuid
import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from shop.models import Order, OrderDesignItem
from shop.forms import OrderForm
from bag.contexts import bag_contents
from profiles.models import UserProfile


# @login_required
def view_bag(request):
    """ A view to return the bag contents page """
    #print("|| bag/views.py || Request Method View Bag: ", request.method)

    return render(request, 'bag/bag.html')

# @login_required
def add_to_bag(request):

    print("|| bag/views.py || Request Method Add to Bag: ", request.method)

    # print("|| bag/views.py || ITEM DICT = ", request.POST.dict())

    bag = request.session.get('bag', {})
    user_order = dict(request.POST.items())
    # print("|| bag/views.py || BAG: ", bag)
    #print("|| bag/views.py || REQUEST CURRENT USER",  request.user)   
    #print("|| bag/views.py || REQUEST USER ORDER",  user_order)   
    bag = user_order
    request.session['bag'] = bag
    return redirect("home")

# @login_required
def remove_from_bag(request, ordered_item):
    # print("\n|| bag/views.py || _______________________________________________")
    print("|| bag/views.py || Request Method Remove from Bag: ", request.method)

    in_bag_order_item = Order.objects.filter(user=request.user)
    print("|| bag/views.py || All ORDERED ITEMS = ", in_bag_order_item, type(in_bag_order_item))

    print("|| bag/views.py || ORDERED ITEM: ", ordered_item, type(ordered_item))
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


# @login_required
def edit_item(request, item_id):
    order = get_object_or_404(Order, id=item_id)
    #print("|| bag/views.py || Request Method Edit Item: ", request.method)

    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'{order.category} order updated successfully')
            return redirect('view_bag')
    form = OrderForm(instance=order)

    #print("|| bag/views.py || EDIT ITEM: ", request)

    context = {
        'form': form
    }

    return render(request, 'bag/edit_item.html', context)


    # bag = request.session.get('bag', {})
    # user_order = dict(request.POST.items())
    # print("|| bag/views.py || BAG: ", bag)
    # print("|| bag/views.py || USER ORDER: ", user_order)
  

    #print("|| bag/views.py || _______________________________________________")

    return redirect(reverse('view_bag'))

# @login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_user = request.user.id
    order_number = request.POST.get('order_number')
    category = request.POST.get('category')
    price = request.POST.get('grand_total')

    #print("|| bag/views.py || REQUEST: ", request.POST.items(), type(request))
    # print("|| bag/views.py || REQUEST Method checkout: ", request.method)
    # print("|| bag/views.py || PRICE: ", order_number)


    if request.method == 'POST':
        
        all_orders = Order.objects.all()
        #print("\n|| bag/views.py || ALL ORDERS: ", all_orders)

        current_bag = bag_contents(request)
        #print("\n|| bag/views.py || CURRENT BAG 1: ", current_bag)

        ordered_item_test = current_bag.get('ordered_item')
        #print("\n|| bag/views.py || CURRENT BAG ordered_item_test: ", ordered_item_test)

        current_bag = current_bag['bag_items']
        #print("\n|| bag/views.py || CURRENT BAG 2: ", current_bag)

        order_item = Order.objects.filter(user=request.user)
        # print("\n|| bag/views.py || ORDER ITEM: ", order_item, type(order_item))
        current_user = request.user.id
        # print("\n|| bag/views.py || CURRENT USER: ", current_user, type(current_user))

        order_form = OrderForm()
        # print("|| bag/views.py || Values ORDER FORM... ", order_form.fields.values())
        
        for order_unit in current_bag:
            #print("\n|| bag/views.py || Order_Unit : ", order_unit.get('ordered_item'), type(order_unit))
            category = order_unit.get('category')
            #print("\n|| bag/views.py || Order_Unit Category: ", category, type(category))
            number_of_concepts = order_unit.get('concept_price')
            #print("\n|| bag/views.py || Order_Unit Number of concepts: ", number_of_concepts, type(number_of_concepts))
            grand_total = order_unit.get('total')
            #print("\n|| bag/views.py || Order_Unit Grand total: ", grand_total, type(grand_total))



            form_data = {
                'user': current_user,
                'category': category,
                'number_of_concepts': number_of_concepts,
                'grand_total': grand_total,
            }

            order_form = OrderForm(form_data)

            # print("\n|| bag/views.py || ORDER FORM: ", order_form)

            if order_form.is_valid():
                print("\n|| bag/views.py || ORDER FORM IS VALID! ", order_form.is_valid())
                order = order_form.save(commit=False)
                order.user = request.user
                order.save()

                if isinstance(item_data, int):
                    order_line_item = OrderDesignItem(
                        order=order_number
                    )

                order_line_item = OrderDesignItem(
                    order=order_unit,
                    category=category,
                    number_of_concepts=number_of_concepts,
                    design_order_total=grand_total,
                )
                order_line_item.save()

            #print("|| bag/views.py || CURRENT BAG: ", current_bag, type(current_bag))
            order_item = Order.objects.filter(user=request.user)
           # print("|| bag/views.py || ORDER ITEM: ", order_item, type(order_item))
           # order_line_item = Order(order_id)

            request.session['save_info'] = 'save_info' in request.POST
     #       print("|| bag/views.py || ORDER ORDER NUMBER: ", order, type(order))
            return redirect('checkout_success')
    else:
        current_bag = bag_contents(request)
        # print("|| bag/views.py || ELSE CURRENT BAG: ", current_bag, type(current_bag))
        messages.error(request, 'There was an error with your order. \
            Please check your information')

        total = current_bag['grand_total']
        #print("|| bag/views.py || TOTAL: ", total, type(total))


        stripe_total = round(total * 100)
        print("|| bag/views.py || STRIPE TOTAL: ", stripe_total, type(stripe_total))
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        #print("|| bag/views.py || STRIPE INTENT: ", intent, type(intent))

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
             Did you forget to set it in your enviroment?')
    
    context = {

        'order_number': order_number,
        'category': category,
        'price': price,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'bag/checkout.html', context)

def checkout_success(request):
    """
    Handels successful checkouts
    """
    current_bag = bag_contents(request)
    current_bag = current_bag['bag_items']

    print("|| bag/views.py checkout_success || REQUEST: ", request.POST.items(), type(request))

    order_item = Order.objects.filter(user=request.user)
    print("|| bag/views.py checkout_success || order_item: ", order_item)
    
    
    

    for ordered_item in order_item:
        print("|| bag/views.py checkout_success || ordered_item: ", ordered_item, type(ordered_item))

        ordered_item.paid=True
        ordered_item.save()
        paid = ordered_item.paid
        
    template = 'bag/checkout_success.html'
    context = {
        'current_bag': current_bag,
    }

    return render(request, template, context)
