from django.contrib.auth.models import AbstractUser
from django.db import models
from product.models import Product


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user.username) + 'cart'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart_item = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='carts')
    location = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=1000000, decimal_places=2, null=True, blank=True, default=0)


class CartItem(BaseModel):
    card = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='cartitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)

