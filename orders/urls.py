from django.urls import path

from .views import *

urlpatterns = [
    path('checkout-order', checkout_order, name='order-checkout'),
    path('create-order', create_order, name='order-create'),
    path('order-created', created_order, name='order-created'),
]