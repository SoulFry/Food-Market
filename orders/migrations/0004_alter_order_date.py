# Generated by Django 4.1.1 on 2023-03-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_itemsinorder_cafe_alter_itemsinorder_dish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]