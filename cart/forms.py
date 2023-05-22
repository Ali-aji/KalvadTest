from django import forms
from django.core.exceptions import ValidationError

from cart.models import Cart, CartItem


class CartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Cart
        fields = "__all__"

    def clean(self, *args, **kwargs):
        self.cleaned_data = super().clean(*args, **kwargs)
        cart = self.cleaned_data["cart"]
        product = self.cleaned_data["product"]
        quantity = self.cleaned_data["quantity"]
        if product.count == 0 and quantity > 0:
            raise ValidationError(f"I'm sorry! But we are out of stock for {product}.")
        if product.count - quantity < 0:
            raise ValidationError(
                f"I'm sorry! But we only have {product.count}KG of {product}."
            )
        return self.cleaned_data
