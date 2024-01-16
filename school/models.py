from django.db import models


class Course(models.Model):  # ViewSet
    title = models.CharField(max_length=300, verbose_name="название")
    image = models.ImageField(upload_to='school/images/', verbose_name='превью(картинка)', null=True, blank=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"


class Lesson(models.Model):  #Generics
    title = models.CharField(max_length=300, verbose_name="название")
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='school/images/', verbose_name='превью(картинка)', null=True, blank=True)
    url = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.title} -- {self.description}'

    class Meta:
        verbose_name = "урок"


