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


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
