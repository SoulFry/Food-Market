from django.urls import path
from FoodSite import settings
import static
from .views import *

urlpatterns = [
    path('', cafes, name='cafes'),
    path('cafe-add', cafeAdd, name='cafe-add'),
    path('<name>', cafemenu, name='cafe-menu'),
    path('<name>/cafe-menu-add', cafeMenuAdd, name='cafe-menu-add'),
    path('comment-add/<cafe>', comment_add, name='comment-add'),
    path('cost-edit/<product>', edit_cost, name='cost-edit')
]