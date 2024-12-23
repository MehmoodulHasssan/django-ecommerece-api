from django.urls import path, include
from .views import ProductsView, LoginUserView, CreateUserView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductsView.as_view(), name='product'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
]