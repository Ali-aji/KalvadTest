from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):

    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.FloatField(validators=[MinValueValidator(0)])
    count = models.PositiveIntegerField(default=0)
    default_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    @property
    def default_line_price(self):
        return self.price * self.default_quantity
