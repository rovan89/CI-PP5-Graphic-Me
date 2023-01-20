import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from shop.models import Order

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


    # bag = request.session.get('bag', {})
    # user_order = dict(request.POST.items())
    # print("|| bag/views.py || BAG: ", bag)
    # print("|| bag/views.py || USER ORDER: ", user_order)
  

    print("|| bag/views.py || _______________________________________________")

    return redirect(reverse('view_bag'))
