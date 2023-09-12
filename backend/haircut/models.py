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
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self) -> str:
        return self.name
