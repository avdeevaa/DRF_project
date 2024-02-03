from celery import shared_task
from django.core.mail import send_mail

from datetime import timedelta
from django.utils import timezone

from config import settings
from school.models import Course
from users.models import User


@shared_task
def check_info_and_update():
    """Рассылка материалов курса."""
    my_mail = "zi_daae@mail.ru"
    for info in Course.objects.all():
        if info.description != info.new_description:
            print(f'Дорогой пользователь, курс обновлен.')
            send_mail(
                subject="обновление курса",
                message=f'Дорогой пользователь, курс обновлен.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[my_mail]

            )
            info.new_description = info.description
            info.save()
            #  it works I'm so happy!!!

# second part - раз в день запускается проверка, если пользователь был на сайте не позднее 30 дней.


# @shared_task если оставить, будет в админке само, если нет, то надо добавлять через copy==copy reference
def check_last_login():
    """Фоновая задача, которая проверяет пользователей по дате последнего входа по полю last_login"""
    today = timezone.now()
    thirty_days_ago = today - timedelta(days=30)
    for user in User.objects.all():
        if user.last_login < thirty_days_ago:
            user.is_active = False
            print("Поменяли пользователя на неактивного.")
            user.save()