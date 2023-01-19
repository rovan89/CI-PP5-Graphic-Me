from django.shortcuts import render, redirect
from .models import Order, OrderDesignItem
from .forms import OrderForm
from django.contrib import messages

def shop_form(request):
    """ This view returns the shop page with form for customers to detail what they want"""
    form = OrderForm()
    form = OrderForm(request.POST, request.FILES)
    print("|| shop/views.py || REQUEST", request.POST)
    print("|| shop/views.py || REQUEST", request.POST)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect('home')
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
    