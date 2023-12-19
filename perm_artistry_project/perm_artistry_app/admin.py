from django.contrib import admin
from .models import Product, Category, Order, UserProfile, CartItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(CartItem)
