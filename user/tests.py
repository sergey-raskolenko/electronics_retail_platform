from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class UserBaseTestCase(APITestCase):
	"""Тест-кейс для регистрации/авторизации пользователя"""
	def setUp(self):
		self.data = {
			'email': 'test@test.test',
			'password': 'test',
		}
		self.user = User.objects.create_user(
			email=self.data['email'], password=self.data['password']
		)

	def test_register(self):
		"""Тест для регистрации нового пользователя"""
		data = {
			'email': 'test1@test.test',
			'password': 'Test1test',
			'password2': 'Test1test',
			'first_name': 'Test',
			'last_name': 'Testov'
		}

		response = self.client.post(reverse('user:register_user'), data=data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(User.objects.get(email=data['email']))

	def test_login(self):
		"""Тест для авторизации пользователя"""
		data = self.data
		response = self.client.post(reverse('user:token_obtain_pair'), data=data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
