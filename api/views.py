from django.shortcuts import render
from rest_framework import generics, permissions, serializers, status, parsers
from rest_framework.response import Response
from .models import Product, Order, OrderItem
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Create your views here.

class ProductsView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    
    def get_queryset(self):
       return Product.objects.only('name', 'price', 'image').order_by('created_at')
    
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

class ProductView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()

class LoginUserView(generics.GenericAPIView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data) # it returns dictionary with refresh and access token if valid, unless raise error
        serializer.is_valid(raise_exception=True)  
        print(serializer.validated_data)      
        
        response = Response(
            {
                "message" : "User logged in successfully.",
                "access_token" : serializer.validated_data["access"],
            }, 
            status=status.HTTP_200_OK
            )
        response.set_cookie(
            key="refresh_token", 
            value=serializer.validated_data["refresh"],
            httponly=True,
            secure=True,
            samesite="None"
        )
        return response


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

class CreateOrderItem(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = OrderItem.objects.all()

    

        


