from django.urls import path, include
from .views import ProductsView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductsView.as_view(), name='product'),
]