from django.db import models

ESTABLISHMENTS_CATEGORY = (
    ('Кафе', 'Кафе'),
    ('Рестораны32', 'Ресторан'),
    ('Пиццерии', 'Пиццерия'),
    ('Азиатская кухня', 'Азиатская кухня'),
    ('Фастфуд', 'ФастФуд'),
)


class CafeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(choices=ESTABLISHMENTS_CATEGORY, max_length=75, unique=True)

    def __str__(self):
        return self.category


class Cafe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, db_index=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/cafes/cafe_images')
    category = models.ForeignKey(CafeCategory, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_total_mark(self):
        self.total_mark = []
        for comment in self.commentcafe_set.all():
            self.total_mark.append(int(comment.mark))
        if len(self.total_mark) != 0:
            return round(sum(self.total_mark)/len(self.total_mark),1)
        else:
            return 0.0


DISH_TYPES = (
    ('Бургеры', 'Бургеры'),
    ('Пицца', 'Пицца'),
    ('Роллы', 'Роллы'),
    ('Закуски', 'Закуски'),
    ('Десерты', 'Десерты'),
    ('Напитки', 'Напитки'),
)


class CafeMenuCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(choices=DISH_TYPES, max_length=75, unique=True)

    def __str__(self):
        return self.category


class CafeMenu(models.Model):
    id_cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75, unique=True, db_index=True)
    ingredients = models.TextField()
    category = models.ForeignKey(CafeMenuCategory, on_delete=models.DO_NOTHING)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='static/images/cafes/delicious_images')

    def __str__(self):
        return self.name
