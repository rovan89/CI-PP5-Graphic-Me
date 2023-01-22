from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_form, name="shop"),
    path('checkout/', views.shop_form, name="checkout"),
]
