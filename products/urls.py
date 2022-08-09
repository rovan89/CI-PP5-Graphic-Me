from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.all_products, name="product"),
    path('product/<int:product_id>', views.portfolio_detail, name="product_detail"),
]
