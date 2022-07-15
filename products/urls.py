from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name="portfolio"),
    path('<int:product_id>', views.portfolio_detail, name="portfolio_detail"),
]
