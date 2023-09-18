from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models import CheckConstraint

from core.constans import (EMAIL_MAX_LENGTH, USERNAME_MAX_LENGTH,
                           PASSWORD_MAX_LENGTH, FIRST_NAME_MAX_LENGTH,
                           LAST_NAME_MAX_LENGTH)
from core.validators import validate_username


class User(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта',
                              max_length=EMAIL_MAX_LENGTH,
                              unique=True,)
    username = models.CharField(verbose_name='Логин',
                                max_length=USERNAME_MAX_LENGTH,
                                validators=(validate_username,),
                                unique=True)
    password = models.CharField(verbose_name='Пароль',
                                max_length=PASSWORD_MAX_LENGTH,
                                )
    first_name = models.CharField(verbose_name='Имя',
                                  max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=(validate_username,))
    last_name = models.CharField(verbose_name='Фамилия',
                                 max_length=LAST_NAME_MAX_LENGTH,
                                 validators=(validate_username,))

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

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
        related_name='subscriber',
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription'),
            CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(from_user=models.F("to_user")),
            ),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
