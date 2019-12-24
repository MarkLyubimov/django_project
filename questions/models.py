from django.db import models
from django.conf import settings


# Create your models here.
DEFAULT_USER_ID = 1


class Articles(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    title = models.CharField("Вопрос", max_length=120)
    post = models.TextField("Подробная формулировка вопроса")
    date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    post = models.TextField("Текст комментария")
    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    article = models.ForeignKey(Articles, related_name='comments', verbose_name=u"!!!!!!!!!", on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title