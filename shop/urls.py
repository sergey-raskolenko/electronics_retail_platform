from django.urls import path
from rest_framework import routers

from shop.apps import ShopConfig
from shop.views import ProductViewSet, ContactViewSet, OrganizationCreateView, OrganizationListView, \
	OrganizationRUDView

app_name = ShopConfig.name

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
	path('org/create/', OrganizationCreateView.as_view(), name='org_create'),
	path('org/', OrganizationListView.as_view(), name='org_list'),
	path('org/<int:pk>/', OrganizationRUDView.as_view(), name='org_rud'),
]

urlpatterns += router.urls
