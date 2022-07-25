from django.contrib import admin
from .models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
