# Generated by Django 4.1.1 on 2023-03-11 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafes', '0007_remove_cafe_slug_alter_cafe_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('id_cafe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafes.cafe')),
                ('id_dishes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafes.cafemenu')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
