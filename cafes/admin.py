from django.contrib import admin
from .models import *

admin.site.register(Cafe)
admin.site.register(CafeMenu)
admin.site.register(CafeCategory)
admin.site.register(CafeMenuCategory)