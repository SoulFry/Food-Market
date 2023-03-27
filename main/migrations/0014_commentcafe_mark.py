# Generated by Django 4.1.1 on 2023-03-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_commentcafe_mark_alter_commentcafe_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentcafe',
            name='mark',
            field=models.CharField(blank=True, choices=[('5', 'Отлично'), ('4', 'Хорошо'), ('3', 'Нормально'), ('2', 'Плохо'), ('1', 'Ужасно')], max_length=10, null=True),
        ),
    ]