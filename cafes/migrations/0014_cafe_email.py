# Generated by Django 4.1.1 on 2023-03-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0013_alter_cafemenu_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
