import uuid
import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from shop.models import Order, OrderDesignItem
from shop.forms import OrderForm
from bag.contexts import bag_contents
from profiles.models import UserProfile


@login_required
def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request):
    """ A view to return the add_to_bag page """
    user_order = dict(request.POST.items())
    bag = user_order
    return redirect("home")


@login_required
def remove_from_bag(request, ordered_item):
    in_bag_order_item = Order.objects.filter(user=request.user)
    try:
        for i in in_bag_order_item:
            item = str(i)

            if item == ordered_item:
                i.delete()
                messages.success(
                    request, f'Item number {i} was removed from bag')
                return render(request, 'bag/bag.html')

    except Exception as e:
        return HttpResponse(status=500)


@login_required
def edit_item(request, item_id):
    order = get_object_or_404(Order, id=item_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{order.category} order updated successfully')
            return redirect('view_bag')
    form = OrderForm(instance=order)

    context = {
        'form': form
    }

    return render(request, 'bag/edit_item.html', context)


@login_required
def checkout(request):
    """ A view to render the checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_user = request.user.id
    order_number = request.POST.get('order_number')
    category = request.POST.get('category')
    price = request.POST.get('grand_total')

    if request.method == 'POST':
        current_bag = bag_contents(request)
        current_bag = current_bag['bag_items']
        order_item = Order.objects.filter(user=request.user)
        current_user = request.user.id
        order_form = OrderForm()

        for order_unit in current_bag:
            category = order_unit.get('category')
            number_of_concepts = order_unit.get('concept_price')
            grand_total = order_unit.get('total')

            form_data = {
                'user': current_user,
                'category': category,
                'number_of_concepts': number_of_concepts,
                'grand_total': grand_total,
            }

            order_form = OrderForm(form_data)

            if order_form.is_valid():
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

            order_item = Order.objects.filter(user=request.user)
            return redirect('checkout_success')
    else:
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

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

    order_item = Order.objects.filter(user=request.user)

    for ordered_item in order_item:

        ordered_item.paid = True
        ordered_item.save()
        paid = ordered_item.paid

    template = 'bag/checkout_success.html'
    context = {
        'current_bag': current_bag,
    }

    return render(request, template, context)
