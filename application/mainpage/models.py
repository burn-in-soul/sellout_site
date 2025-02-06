from django.db import models


class MainpageImages(models.Model):
    image = models.ImageField(upload_to='images')

    class Meta:
        db_table = 'meinpage_images'
        verbose_name = 'Картинка для главной'
        verbose_name_plural = 'Картинки для главной'
