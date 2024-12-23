from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'image', 'created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)

# Register your models here.
