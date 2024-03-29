# Generated by Django 5.0.1 on 2024-01-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='статус оплаты'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='id сессии'),
        ),
    ]
