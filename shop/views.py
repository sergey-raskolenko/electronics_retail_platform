from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters
from user.permissons import IsActive

from shop.serializers import ProductSerializer, ContactSerializer, OrganizationSerializer, OrganizationRUDSerializer
from shop.models import Product, Contact, Organization


class ProductViewSet(viewsets.ModelViewSet):
	"""
	Контроллер вьюсет для работы с объектами модели Product
	"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
	"""
	Контроллер вьюсет для работы с объектами модели Contact
	"""
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	permission_classes = [IsActive]


class OrganizationCreateView(generics.CreateAPIView):
	"""
	Контроллер для создания объекта модели Organization
	"""
	queryset = Contact.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = [IsActive]


class OrganizationListView(generics.ListAPIView):
	"""
	Контроллер для детального просмотра, изменения, удаления объекта модели Organization
	"""
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = [IsActive]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['contacts__country']
	search_fields = ['contacts__country']


class OrganizationRUDView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Контроллер для просмотра списка объектов модели Organization
	"""
	queryset = Organization.objects.all()
	serializer_class = OrganizationRUDSerializer
	permission_classes = [IsActive]
