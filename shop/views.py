from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from shop.serializers import ProductSerializer, ContactSerializer, OrganizationSerializer, OrganizationRUDSerializer
from shop.models import Product, Contact, Organization


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]


class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	permission_classes = [AllowAny]


class OrganizationCreateView(generics.CreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = [AllowAny]


class OrganizationListView(generics.ListAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = [AllowAny]


class OrganizationRUDView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationRUDSerializer
	permission_classes = [AllowAny]

