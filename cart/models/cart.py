from django.db import models
from .customer import Customer


class Cart(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
