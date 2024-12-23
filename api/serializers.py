from rest_framework import serializers, status
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"
        