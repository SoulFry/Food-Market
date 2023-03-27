from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager
from cafes.models import *


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='static/images/users/avatars', default='static/images/users/avatars/default_logo_user.jpg')
    balance = models.IntegerField(default=0)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True


MARK_CHOICE = (
    ('5', 'Отлично'),
    ('4', 'Хорошо'),
    ('3', 'Нормально'),
    ('2', 'Плохо'),
    ('1', 'Ужасно'),
)


class CommentCafe(models.Model):
    subject = models.CharField(max_length=200)
    to_cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    mark = models.CharField(choices=MARK_CHOICE, max_length=10)
    public_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def get_mark(self):
        return self.mark
