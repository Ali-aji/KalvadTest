from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Cart, CartItem, Product


def index(request):
    context = {}
    return render(request, 'base.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        items = cart.cartitem_set.all()
    else:
        items = []
        cart = {'get_cart_total':0, 'get_cart_items':0}


    context = {'items': items, 'cart': cart}
    return render(request, 'cart.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	cart, created = Cart.objects.get_or_create(customer=customer, complete=False)

	cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)

	if action == 'add':
		cartItem.quantity = (cartItem.quantity + 1)
	elif action == 'remove':
		cartItem.quantity = (cartItem.quantity - 1)

	cartItem.save()

	if cartItem.quantity <= 0:
		cartItem.delete()

	return JsonResponse('Item was added', safe=False)
