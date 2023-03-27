# Generated by Django 4.0.5 on 2022-08-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('description', models.TextField(blank=True, db_index=True)),
                ('image', models.ImageField(upload_to='static/images/cafes')),
            ],
        ),
    ]
