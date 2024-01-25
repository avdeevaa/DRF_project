# Generated by Django 5.0.1 on 2024-01-19 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='school.course', verbose_name='lesson'),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='пользователь')),
                ('payment_date', models.DateField(auto_now=True, verbose_name='дата оплаты')),
                ('amount', models.IntegerField(max_length=6, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'CASH'), ('card', 'CARD')], default='card', verbose_name='способ оплаты')),
                ('course_paid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='school.course', verbose_name='course')),
                ('lesson_paid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='school.lesson', verbose_name='lesson')),
            ],
        ),
    ]