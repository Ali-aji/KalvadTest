from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.FloatField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
