from django.shortcuts import render, redirect

from products.models import Product
from shop.models import Order
from shop.forms import OrderForm


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request):

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    user_order = dict(request.POST.items())
    bag = user_order
    request.session['bag'] = bag
    print(request.session['bag']
    return redirect(redirect_url)
