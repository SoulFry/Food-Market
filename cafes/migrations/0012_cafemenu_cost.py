# Generated by Django 4.1.1 on 2023-03-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0011_alter_cafe_category_alter_cafemenu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafemenu',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
