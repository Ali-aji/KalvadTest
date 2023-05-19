from django.contrib import admin
from cart import models


class CartAdmin(admin.ModelAdmin):
    list_display = ["__str__", "display_total"]

    @admin.display(description='Total')
    def display_total(self, obj):
        return obj.get_total


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "quantity", "display_total"]

    @admin.display(description='Total')
    def display_total(self, obj):
        return obj.get_total


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "count", "price"]