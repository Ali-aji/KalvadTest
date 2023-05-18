from django.shortcuts import render
from .models import Cart


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
