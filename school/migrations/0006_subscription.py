# Generated by Django 5.0.1 on 2024-01-26 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_course_owner_lesson_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription', models.BooleanField(default=False, verbose_name='Подписка?')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subscribed', to='school.course', verbose_name='course_subscribed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscribed', to=settings.AUTH_USER_MODEL, verbose_name='user_subscribed')),
            ],
            options={
                'verbose_name': 'платеж',
                'unique_together': {('user', 'course')},
            },
        ),
    ]
