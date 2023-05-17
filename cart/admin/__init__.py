from django.contrib import admin
from cart import models

admin.site.register(models.Customer)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Product)
