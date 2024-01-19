from django.core.exceptions import ValidationError
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
		unique_together = (('email', 'country', 'city', 'street', 'house_number'),)


class Product(models.Model):
	"""
	Модель продукта
	"""
	name = models.CharField(max_length=50, verbose_name='Название')
	model = models.CharField(max_length=50, verbose_name='Модель', **NULLABLE)
	release_date = models.DateField(max_length=50, verbose_name='Дата выхода на рынок', **NULLABLE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"
		db_table = 'products'
		unique_together = (('name', 'model'),)


class OrganizationChoices(models.TextChoices):

	FACTORY = 'F', 'Завод'
	RETAIL = 'R', 'Розничная сеть'
	IE = 'IE', 'Индивидуальный предприниматель'


class Organization(models.Model):
	organization_type = models.CharField(
		max_length=2, choices=OrganizationChoices.choices, verbose_name='Тип организации'
	)
	hierarchy_level = models.PositiveSmallIntegerField(verbose_name='Уровень в иерархии', **NULLABLE)
	name = models.CharField(unique=True, max_length=50, verbose_name='Название организации')
	contacts = models.ForeignKey(
		Contact, on_delete=models.CASCADE, related_name='contacts', verbose_name='Контакты'
	)
	supplier = models.ForeignKey(
		'self', on_delete=models.CASCADE, related_name='suppliers', verbose_name='Поставщик', **NULLABLE
	)
	product = models.ManyToManyField(
		Product, related_name='products', verbose_name=''
	)
	debt = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Долг перед поставщиком')
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = "Организация"
		verbose_name_plural = "Организации"
		db_table = 'organizations'
		ordering = ('hierarchy_level', 'name',)

	def __str__(self):
		return self.name

	def clean(self):
		if self.organization_type == OrganizationChoices.FACTORY and self.supplier:
			raise ValidationError("Factory doesn't have suppliers")

		if not self.supplier and self.debt > 0:
			raise ValidationError("Factory can't have a dept")

	def save(self, *args, **kwargs):
		if self.organization_type == OrganizationChoices.FACTORY:
			self.hierarchy_level = 0
		elif self.supplier and self.supplier.hierarchy_level == 0:
			self.hierarchy_level = 1
		else:
			self.hierarchy_level = 2
		super().save(*args, **kwargs)
