# Generated by Django 4.1.1 on 2023-03-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/users/avatars/default_logo_user.jpg', upload_to='static/images/users/avatars'),
        ),
    ]
