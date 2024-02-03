#  здесь мы создаем отложенную задачу,
#  то есть добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from school.models import Course


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


