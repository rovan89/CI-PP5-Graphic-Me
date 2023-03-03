from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category

# Create your views here.


def full_portfolio(request):
    """ This view returns the portfolio page,
    including sorting and search queries"""

    portfolio_items = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            portfolio_items = portfolio_items.filter(
                category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a vald search input")
                return redirect(reverse('portfolio_items'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            portfolio_items = portfolio_items.filter(queries)

    context = {
        'portfolio_items': portfolio_items,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, product_id):
    """ This view returns the detailed page for individual portfolio items """

    portfolio_item = get_object_or_404(Product, pk=product_id)

    context = {
        'portfolio_item': portfolio_item,
    }

    return render(request, 'portfolio/portfolio_detail.html', context)
