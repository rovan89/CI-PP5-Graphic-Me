from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def shop_form(request):
    """ This view returns the shop page with form for customers to detail what they want"""
    
    form = OrderForm()

    context = {
        'form': form
    }

    return render(request, 'shop/shop_main.html', context)


def chekout(request, order_number):

    order_number = request.POST.get('order_number')
    category = request.POST.get('category')
    number_of_concepts = int(request.POST.get('number_of_concepts'))
    price = request.POST.get('price')

    context = {
        'order_number': order_number,
        'category': category,
        'number_of_concepts': number_of_concepts,
        'price': price,
    }

    return render(request, 'shop/checkout.html', context)
    