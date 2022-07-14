from django.shortcuts import render

# Create your views here.

def portfolio(request):
    """ This view returns the portfolio page """

    return render(request, 'products/portfolio.html')
