from rest_framework import serializers, status
from .models import Product, Order, OrderItem
from django.contrib.auth.models import User
from PIL import Image

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"

    def validate_price(self, value):
            print(int(value))
            if float(value) < 10:
                raise serializers.ValidationError("Price must be greater than 10")
            return value
    def validate_image(self, value):
            print(type(value))
            Image.open(value).verify()            
            if value.size > 2 * 1024 * 1024: # 2MB
                raise serializers.ValidationError("Image size must be less than 1MB")
            return value

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'in_stock']
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'order_items')

    
    


