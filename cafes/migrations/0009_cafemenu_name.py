# Generated by Django 4.1.1 on 2023-03-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0008_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafemenu',
            name='name',
            field=models.CharField(max_length=75, null=True, unique=True),
        ),
    ]