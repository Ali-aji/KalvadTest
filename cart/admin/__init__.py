from django.contrib import admin
from cart import models
from .models_admin import CartAdmin, CartItemAdmin, ProductAdmin


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Product, ProductAdmin)

