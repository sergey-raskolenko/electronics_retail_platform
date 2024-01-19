from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import UserManager

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
	"""
	Модель пользователя
	"""
	objects = UserManager()

	username = None
	email = models.EmailField(unique=True, verbose_name='Электронная почта', max_length=254)
	first_name = models.CharField(max_length=64, verbose_name="Имя")
	last_name = models.CharField(max_length=64, verbose_name="Фамилия")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		db_table = 'users'

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
