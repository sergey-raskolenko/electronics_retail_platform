from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from shop.models import Product, Contact
from user.models import User


class ProductTestCase(APITestCase):
	"""Тест-кейс для контроллер-вьюсета продукта"""

	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(email='test@test.test', password='test')
		self.client.force_authenticate(user=self.user)

		self.data = {
			'name': 'test@test.test',
			'model': 'test',
		}
		self.product = Product.objects.create(
			name=self.data['name'], model=self.data['model']
		)

	def test_list_product(self):
		response = self.client.get(reverse('shop:product-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(Product.objects.all().count() == 1)

	def test_create_product(self):
		data = {
			'name': 'test@test.test1',
			'model': 'test1',
		}
		response = self.client.post(reverse('shop:product-list'), data=data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(Product.objects.all().count() == 2)

	def test_rud_product(self):
		data = {
			'model': 'test1',
		}
		response = self.client.get(reverse('shop:product-detail', args=[self.product.pk]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.patch(reverse('shop:product-detail', args=[self.product.pk]), data=data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(Product.objects.get(pk=self.product.pk).model == data['model'])
		response = self.client.delete(reverse('shop:product-detail', args=[self.product.pk]))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Product.objects.filter(name=self.data['name']))


class ContactTestCase(APITestCase):
	"""Тест-кейс для контроллер-вьюсета контакта"""

	def setUp(self):
		self.client = APIClient()
		self.user = User.objects.create_user(email='test@test.test', password='test')
		self.client.force_authenticate(user=self.user)

		self.data = {
			'email': 'test@test.test',
			'country': 'test',
		}
		self.contact = Contact.objects.create(
			email=self.data['email'], country=self.data['country']
		)

	def test_list_product(self):
		response = self.client.get(reverse('shop:contact-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(Contact.objects.all().count() == 1)

	def test_create_product(self):
		data = {
			'email': 'test@test.test1',
			'country': 'test1',
			'city': 'test1',
			'street': 'test1',
			'house_number': 'test1'
		}
		response = self.client.post(reverse('shop:contact-list'), data=data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(Contact.objects.all().count() == 2)

	def test_rud_product(self):
		data = {
			'country': 'test1',
		}
		response = self.client.get(reverse('shop:contact-detail', args=[self.contact.pk]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.patch(reverse('shop:contact-detail', args=[self.contact.pk]), data=data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(Contact.objects.get(pk=self.contact.pk).country == data['country'])
		response = self.client.delete(reverse('shop:contact-detail', args=[self.contact.pk]))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Contact.objects.filter(email=self.data['email']))
