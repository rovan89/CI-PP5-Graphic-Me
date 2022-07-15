from django.shortcuts import render
from .models import Product

# Create your views here.

def portfolio(request):
    """ This view returns the portfolio page, including sorting and search quries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/portfolio.html', context)
