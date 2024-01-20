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

	def test_create_su(self):
		data = {
			'email': 'admin@admin.admin',
			'password': 'Adminadmin',
			'first_name': 'Admin',
			'last_name': 'Admin'
		}
		User.objects.create_superuser(**data)
		csu = User.objects.get(email=data['email'])
		self.assertTrue(csu)
		self.assertTrue(csu.is_staff)
		self.assertTrue(csu.is_superuser)

		try:
			User.objects.create_superuser(**data, is_staff=False)
		except ValueError as e:
			assert e

		try:
			User.objects.create_superuser(**data, is_superuser=False)
		except ValueError as e:
			assert e

