from django.db import models


class Concert(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=1024,
        null=False,
        blank=False
    )
    start_datetime = models.DateTimeField(
        verbose_name='Время начала',
        null=False,
        blank=False,
    )
    end_datetime = models.DateTimeField(
        verbose_name='Время начала',
        null=True,
        blank=True,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=1024,
        null=False,
        blank=False,
    )
    vk_event = models.CharField(
        verbose_name='Встреча ВК',
        max_length=1024,
        null=True,
        blank=True,
    )
    tickets_link = models.CharField(
        verbose_name='Ссылка на билеты',
        max_length=2048,
        null=False,
        blank=False,
    )
    poster = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'concerts'
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
