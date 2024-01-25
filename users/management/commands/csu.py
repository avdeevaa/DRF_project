from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.com",
            first_name="Admin",
            last_name="Adminov",
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345adminka')
        user.save()


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjI3NzcxNCwiaWF0IjoxNzA2MTkxMzE0LCJqdGkiOiJjYWFjMzhiOTViNjQ0YWMwOTcxNTQ1ZjkxNjVkNjIxOCIsInVzZXJfaWQiOjF9._NGpHHejRlpEcAz4ogbCNbkHQFvPeNhQDSzPMJXgYeE",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MTkxNjE0LCJpYXQiOjE3MDYxOTEzMTQsImp0aSI6Ijk4NTMxYTVhNmYwYTRhODNhMTMyYjc5YTQ0YmQ2YTY0IiwidXNlcl9pZCI6MX0.NKU7U_OfBgyCaA7xydzoaOL8XNYkD04cinVC4CYRubM"
# }