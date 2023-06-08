from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя',
                            validators=[RegexValidator(r"^[а-яА-Я- ]+$", message="Разрешена только кириллица"), ], )
    surname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия',
                               validators=[RegexValidator(r"^[а-яА-Я- ]+$", message="Разрешена только кириллица"), ], )
    username = models.CharField(max_length=100, blank=False, verbose_name='Логин', unique=True, validators=[
        RegexValidator(r"^[a-zA-Z0-9-]+$", message="Разрешена только латиница"), ], )
    email = models.EmailField(max_length=100, blank=False, verbose_name='Почта', unique=True)
    password = models.CharField(max_length=100, blank=False, verbose_name='Пароль')
    rules = models.CharField(max_length=100, blank=True, verbose_name='Правила')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Pool(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя', )
    age = models.CharField(max_length=100, blank=True, verbose_name='Фамилия', )
    nickname = models.CharField(max_length=100, blank=False, verbose_name='Логин', unique=True, )
    elo = models.EmailField(max_length=100, blank=False, verbose_name='Эло', )
    hours = models.CharField(max_length=100, blank=False, verbose_name='Часы')
    discord = models.CharField(max_length=100, blank=True, verbose_name='Дискорд', unique=True)

    def __str__(self):
        return self.nickname
