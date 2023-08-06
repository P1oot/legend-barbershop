from django.db import models
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

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
