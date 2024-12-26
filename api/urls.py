from django.urls import path, include
from .views import CreateProductsView, LoginUserView, CreateUserView, ListProductsView, ListOrders, ProductInfoView

urlpatterns = [
    path('create-product/', CreateProductsView.as_view(), name='create-product'),
    path('list-products/', ListProductsView.as_view(), name='list-products'),
    # path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    # path('api-auth/', include('rest_framework.urls')),
    path('list-orders/', ListOrders.as_view(), name='list-orders'),
    path('products-info/', ProductInfoView.as_view(), name= 'products-info')
]