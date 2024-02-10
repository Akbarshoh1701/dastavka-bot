from django.contrib import admin

# Register your models here.
from user.models import User, Cart, Order, CartItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'phone', 'language']
    list_display_links = ['id', 'username', 'phone', 'language']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cart']
    list_display_links = ['id', 'user', 'cart']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'card']
    list_display_links = ['id', 'card']


