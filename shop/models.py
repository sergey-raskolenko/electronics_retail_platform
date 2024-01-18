from django.db import models

from user.models import NULLABLE


class Contact(models.Model):
	"""
	Модель контактов, основная информация об адресе.
	"""
	email = models.EmailField(max_length=255, verbose_name='Адрес почты')
	country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
	city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
	street = models.CharField(max_length=50, verbose_name='Улица', **NULLABLE)
	house_number = models.CharField(max_length=10, verbose_name='Номер дома', **NULLABLE)

	def __str__(self):
		return f"{self.email}:{self.country}, {self.city}, st.{self.street} {self.house_number}"

	class Meta:
		verbose_name = "Контакт"
		verbose_name_plural = "Контакты"
		db_table = 'contacts'
		unique_together = (('email', 'country', 'city', 'name'),)


class Product(models.Model):
	"""
	Модель продукта
	"""
	name = models.CharField(max_length=50, verbose_name='Название')
	model = models.CharField(max_length=50, verbose_name='Модель', **NULLABLE)
	release_date = models.DateField(max_length=50, verbose_name='Дата выхода на рынок', **NULLABLE)

	def __str__(self):
		return f"{self.name} {self.model}"

	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"
		db_table = 'products'
		unique_together = (('name', 'model'),)
