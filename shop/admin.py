from django.contrib import admin
from .models import Order, OrderDesignItem

class OrderDesignItemAdminInline(admin.TabularInline):
    model = OrderDesignItem
    readonly_fields = ('design_order_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderDesignItemAdminInline,)

    readonly_fields = (
        'order_number',
        'category',
        'number_of_concepts',
        'price',
        'created_on',
    )
    
    list_display = (
        'id',
        'order_number',
        'user',
        'category',
        'number_of_concepts',
        'price',
        'created_on',
    )

    ordering =('-created_on',)

admin.site.register(Order, OrderAdmin)
