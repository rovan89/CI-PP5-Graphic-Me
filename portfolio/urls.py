from django.urls import path
from . import views

urlpatterns = [
    path('', views.full_portfolio, name="portfolio"),
    path('portfolio/<int:product_id>', views.portfolio_detail, name="portfolio_detail"),
]
