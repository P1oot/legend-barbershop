from django.db import models


class Services(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='руб.',
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=500,
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self) -> str:
        return self.name


class Haircuts(models.Model):
    image = models.ImageField(
        verbose_name='Стрижка',
        upload_to='img/',
    )

    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Стрижки'


class Promotions(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=500,
    )

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
