from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer

# Create your views here.

class ProductsView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.only('name', 'price', 'image').order_by('created_at')

class ProductView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()


