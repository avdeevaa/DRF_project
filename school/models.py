from django.db import models

from config import settings
from users.models import User


class Course(models.Model):  # ViewSet
    title = models.CharField(max_length=300, verbose_name="название")
    image = models.ImageField(upload_to='school/images/', verbose_name='превью(картинка)', null=True, blank=True)
    description = models.TextField(verbose_name='описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"


class Lesson(models.Model):  #Generics
    title = models.CharField(max_length=300, verbose_name="название")
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='school/images/', verbose_name='превью(картинка)', null=True, blank=True)
    url = models.URLField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', verbose_name='lesson', null=True, blank=True)  # чтобы привязывалось
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} -- {self.description}'

    class Meta:
        verbose_name = "урок"


class Payments(models.Model):

    PAYMENT_METHODS = [
        ('cash', 'CASH'),
        ('card', 'CARD'),
    ]

    user = models.CharField(max_length=50, verbose_name='пользователь')  # предполагаю, потом нужно будет связать с пользователем из Users
    payment_date = models.DateField(verbose_name='дата оплаты', auto_now=True)

    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', verbose_name='course', blank=True, null=True)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson', verbose_name='lesson', blank=True, null=True)

    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты', choices=PAYMENT_METHODS, default='card')

    def __str__(self):
        return f'{self.user} paid {self.amount}'

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"


class Subscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_subscribed", related_name='user_subscribed')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course_subscribed", related_name='course_subscribed')
    subscription = models.BooleanField(verbose_name="Подписка?", default=False)

    def __str__(self):
        return f'{self.user} and {self.course}'

    class Meta:
        unique_together = ['user', 'course']
        verbose_name = "платеж"


