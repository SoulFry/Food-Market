from django.db import models

from main.models import User
from cafes.models import Cafe, CafeMenu


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Order {}'.format(self.order_number)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.itemsinorder_set.all())


class ItemsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.DO_NOTHING)
    dish = models.ForeignKey(CafeMenu, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cost * self.count

