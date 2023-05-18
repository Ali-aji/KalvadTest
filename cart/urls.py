
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="base"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item")
]
