from django.contrib.auth import get_user_model
from django.db import models


class Cart(models.Model):

    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_total(self):
        cart_items = self.items.all()
        total = sum([item.get_total for item in cart_items])
        return total 

    @property
    def get_items(self):
        cart_items = self.items.all()
        total = sum([item.quantity for item in cart_items])
        return total 
