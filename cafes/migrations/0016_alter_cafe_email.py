# Generated by Django 4.1.1 on 2023-03-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0015_alter_cafe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]