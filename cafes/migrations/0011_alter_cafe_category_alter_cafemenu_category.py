# Generated by Django 4.1.1 on 2023-03-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0010_cafe_category_cafemenu_category_alter_cafemenu_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='category',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='cafemenu',
            name='category',
            field=models.CharField(max_length=75),
        ),
    ]
