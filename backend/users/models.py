from django.contrib.auth.models import AbstractUser
from django.db import models
from core.validators import validate_username
from django.db.models import UniqueConstraint


class User(AbstractUser):
    EMAIL_MAX_LENGTH = 254
    USERNAME_MAX_LENGTH = 150
    PASSWORD_MAX_LENGTH = 150
    FIRST_NAME_MAX_LENGTH = 150
    LAST_NAME_MAX_LENGTH = 150
    email = models.EmailField(verbose_name="Электронная почта",
                              max_length=EMAIL_MAX_LENGTH,
                              unique=True,)
    username = models.CharField(verbose_name="Логин",
                                max_length=USERNAME_MAX_LENGTH,
                                validators=(validate_username,),
                                unique=True)
    password = models.CharField(verbose_name="Пароль",
                                max_length=PASSWORD_MAX_LENGTH,
                                )
    first_name = models.CharField(verbose_name="Имя",
                                  max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(validate_username,))
    last_name = models.CharField(verbose_name="Фамилия",
                                 max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(validate_username,))

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username

class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name="Подписчик",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='subscribing',
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
