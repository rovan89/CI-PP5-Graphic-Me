from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def portfolio(request):
    """ This view returns the detailed page for individual portfolio items """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/portfolio.html', context)


def portfolio_detail(request, product_id):
    """ This view returns the portfolio page, including sorting and search quries"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/portfolio_detail.html', context)
