# Generated by Django 4.1.1 on 2023-03-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0026_alter_cafecategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafecategory',
            name='category',
            field=models.CharField(choices=[('Кафе', 'Кафе'), ('Рестораны32', 'Ресторан'), ('Пиццерии', 'Пиццерия'), ('Азиатская кухня', 'Азиатская кухня'), ('Фастфуд', 'ФастФуд')], max_length=75, unique=True),
        ),
    ]
