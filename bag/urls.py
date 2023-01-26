from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_bag, name="add_to_bag"),
    path('delete/<ordered_item>/', views.remove_from_bag, name="remove_from_bag"),
    path('edit/<item_id>/', views.edit_item, name="edit"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout_success/', views.checkout_success, name="checkout_success"),
    path('', views.view_bag, name="view_bag"),
]