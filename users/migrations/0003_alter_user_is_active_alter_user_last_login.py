# Generated by Django 5.0.1 on 2024-02-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный пользователь?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default='2024-01-01', verbose_name='Дата последней активности'),
        ),
    ]
