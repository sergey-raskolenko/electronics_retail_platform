from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import Product, Contact, Organization, OrganizationChoices


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organization
		fields = '__all__'

	def validate(self, attrs):
		if attrs.get('organization_type') == OrganizationChoices.FACTORY and attrs.get('supplier'):
			raise ValidationError("Factory doesn't have suppliers")

		if not attrs.get('supplier') and attrs.get('debt') > 0:
			raise ValidationError("Factory can't have a dept")

		return attrs


class OrganizationRUDSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=True, read_only=True)
	contacts = ContactSerializer(many=False, read_only=True)

	class Meta:
		model = Organization
		fields = '__all__'
		read_only_fields = ('debt',)
