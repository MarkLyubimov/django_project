from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
DEFAULT_ID = 1


class Articles(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_ID)
    title = models.CharField("Вопрос", max_length=120, default='?')
    post = models.TextField("Подробная формулировка вопроса", default='')
    date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Comments(models.Model):
    postassigned = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments', default=DEFAULT_ID)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_ID)
    text = models.TextField(default='')
    date = models.DateTimeField("Дата публикации", default=timezone.now)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
