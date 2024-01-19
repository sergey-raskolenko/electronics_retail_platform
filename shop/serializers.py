from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import Product, Contact, Organization, OrganizationChoices


class ProductSerializer(serializers.ModelSerializer):
	"""
	Сериализатор для модели Product
	"""
	class Meta:
		model = Product
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	"""
	Сериализатор для модели Contact
	"""
	class Meta:
		model = Contact
		fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
	"""
	Базовый сериализатор для модели Organization
	"""
	class Meta:
		model = Organization
		fields = '__all__'

	def validate(self, attrs):
		"""
		Валидация данных по принципам:
		1) Завод не может иметь поставщика
		2) Завод не может иметь долг
		"""
		if attrs.get('organization_type') == OrganizationChoices.FACTORY and attrs.get('supplier'):
			raise ValidationError("Factory doesn't have suppliers")

		if attrs.get('organization_type') == OrganizationChoices.FACTORY and attrs.get('debt') > 0:
			raise ValidationError("Factory can't have a dept")

		return attrs


class OrganizationRUDSerializer(serializers.ModelSerializer):
	"""
	Сериализатор для детального просмотра, изменения, удаления объекта модели Organization
	"""
	product = ProductSerializer(many=True, read_only=True)
	contacts = ContactSerializer(many=False, read_only=True)

	class Meta:
		model = Organization
		fields = '__all__'
		read_only_fields = ('debt',)
