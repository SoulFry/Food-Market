from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include('main.urls')),
    path('cafes/', include('cafes.urls')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]
