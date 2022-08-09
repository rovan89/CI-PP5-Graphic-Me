from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_bag, name="add_to_bag"),
    path('', views.view_bag, name="view_bag"),
]