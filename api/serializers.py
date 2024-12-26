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
    #if we have to show the product details in the order item then we can use the below line
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'sub_total')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True )
    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'order_items')

#lets define a generic serializer where we can check info about products

class ProductInfoSerializer(serializers.Serializer):
    products = ProductListSerializer(many=True)
    count = serializers.IntegerField(read_only=True)
    max_price = serializers.FloatField(read_only=True)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     print(representation)
    #     products = instance['products']
    #     representation['count'] = len(products)
    #     representation['max_price'] = max(product['price'] for product in products)
    #     return representation
        
