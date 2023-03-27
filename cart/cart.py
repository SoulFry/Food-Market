from decimal import Decimal
from django.conf import settings
from cafes.models import CafeMenu

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, object, count, update_count=False):
        object_id = str(object.id)
        if object_id not in self.cart:
            self.cart[object_id] = {
                'count': 1,
                'cost': str(object.cost)
            }
        if not update_count:
            self.cart[object_id]['count'] = count
        else:
            self.cart[object_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, object):
        object_id = str(object.id)
        if object_id in self.cart:
            del self.cart[object_id]
            self.save()

    def __iter__(self):
        object_list = self.cart.keys()
        objects = CafeMenu.objects.filter(id__in=object_list)
        for object in objects:
            self.cart[str(object.id)]['object'] = object

        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost']*item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.cart.values())

    def get_total_cost(self):
        return sum(Decimal(item['cost'])*item['count'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True