from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'image', 'created_at']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, inlines=[OrderItemInline])
admin.site.register(OrderItem , OrderItemAdmin)

# Register your models here.
