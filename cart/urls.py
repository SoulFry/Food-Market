from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail, name='cart-detail'),
    path('add/<object_id>', cart_add, name='cart-add'),
    path('remove/<object_id>', cart_remove, name='cart-remove'),
]