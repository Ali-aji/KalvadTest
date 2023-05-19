
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="base"),
    path('', views.cart, name="cart"),
]
