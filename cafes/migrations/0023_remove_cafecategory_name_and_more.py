# Generated by Django 4.1.1 on 2023-03-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0022_alter_cafecategory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafecategory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cafemenucategory',
            name='name',
        ),
        migrations.AlterField(
            model_name='cafecategory',
            name='category',
            field=models.CharField(choices=[('1', 'Кафе'), ('2', 'Ресторан'), ('3', 'Пиццерия'), ('4', 'Азиатская кухня'), ('5', 'ФастФуд')], max_length=75, unique=True),
        ),
        migrations.AlterField(
            model_name='cafemenucategory',
            name='category',
            field=models.CharField(choices=[('1', 'Бургеры'), ('2', 'Пицца'), ('3', 'Роллы'), ('4', 'Закуски'), ('5', 'Десерты'), ('6', 'Напитки')], max_length=75, unique=True),
        ),
    ]
