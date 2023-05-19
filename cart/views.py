import json
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CartForm
from .models import Cart, CartItem, Product



def index(request):
	context = {}
	return render(request, 'base.html', context)

@login_required
def cart(request, cart_id=None):
	_cart = None
	items = []
	errors = []
	formset = None
	products = Product.objects.filter(count__gt=0)
	customer = request.user
	if request.method == "GET":
		cart_item_formset = forms.inlineformset_factory(
			Cart, CartItem, fields="__all__",
			extra=len(products),
		)
		formset = cart_item_formset()
		for form, product in zip(formset.forms, products):
			form.initial = {
				"product": product,
				"quantity": product.default_quantity
			}
	if request.method == "POST":
		_cart, created = Cart.objects.get_or_create(
			customer=customer, id=cart_id)
		formset = forms.inlineformset_factory(
			Cart, CartItem, fields="__all__",
			form=CartForm,
		)(request.POST, instance=_cart)
		if formset.is_valid():
			formset.save()
			items = CartItem.objects.filter(
				id__in=_cart.items.values_list("id"))
			products = []
			for item in items:
				product = item.product
				product.count = product.count - item.quantity
				product.save()
				item.save()
				products.append(product)
			_cart.complete = True
			_cart.save()
			messages.success(
				request, "Successfuly confirmed!")
		else:
			errors = [
				error for error_dict in formset.errors
				for error in error_dict.values()
			]
			for error in errors:
				messages.add_message(
					request, messages.ERROR, error,
					fail_silently=True,
				)
	context = {
		'items': items,
		'cart': _cart,
		"products": products,
		"formset": formset,
	}
	return render(request, 'cart.html', context)
