from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    avatar = models.ImageField(upload_to='users/images/', verbose_name="Аватар", null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name="Номер телефона", null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name="Город", default="Moscow")

    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь?')
    last_login = models.DateField(default='2024-01-01', verbose_name='Дата последней активности')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # так мы настраиваем, чтобы емаил стал главным полем для авторизации
