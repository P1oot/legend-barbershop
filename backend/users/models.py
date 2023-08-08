from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'user'),
        (ADMIN, 'admin'),
    ]
    role = models.CharField(
        max_length=20,
        verbose_name='Роль',
        help_text='Роль пользователя',
        choices=ROLE_CHOICES,
        default=USER,
    )
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Телефон',
        help_text='Введите номер телефона'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
