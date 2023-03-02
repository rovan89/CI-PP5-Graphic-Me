from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDesignItem
from .forms import OrderForm
from django.contrib import messages

@login_required
def shop_form(request):
    """ This view returns the shop page with form for customers to detail what they want"""
    current_user = request.user.id
    form = OrderForm()
    form = OrderForm( request.POST, request.FILES)
    print("|| shop/views.py || REQUEST", request.POST)
    print("|| shop/views.py || REQUEST", request.POST)

   
    context = {
        'current_user': current_user,
        'form': form
    }

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            # print("|| shop/views.py || REQUEST CURRENT USER",  user_form.user)

            user_form.save()
            messages.success(request, f'Order successfully added to bag')
            return redirect('home')
    return render(request, 'shop/shop_main.html', context)

    