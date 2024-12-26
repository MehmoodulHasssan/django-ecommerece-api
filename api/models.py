from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name


class Order(models.Model): 
    # StatusChoices = {
    #     "P" : "pending",
    #     "S" : "successfull",
    #     "D"  : "declined"
    # }
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders") #its many to one relationship
    products = models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id } by @{self.customer.username}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def sub_total(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{str(self.quantity)} {self.product.name}{self.quantity > 1 and 's' or ''} in order {self.order.id}"


    