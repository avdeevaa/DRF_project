import re

from rest_framework.serializers import ValidationError


class URLValidator:
    """Реализует дополнительную проверку на отсутствие
    в материалах ссылок на сторонние ресурсы, кроме github, sky.pro.
    Youtube я делать не стала, ибо в моей бд нет ссылок на ютуб"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        allowed_domains = ["github", "my.sky.pro"]
        tmp_val = dict(value).get(self.field)

        if not any(domain in tmp_val for domain in allowed_domains):
            raise ValidationError('Bad URL address')
