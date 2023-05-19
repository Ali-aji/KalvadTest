from django.core.exceptions import ValidationError
from django.db import models
from .cart import Cart
from .product import Product


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.product}({self.cart})"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
