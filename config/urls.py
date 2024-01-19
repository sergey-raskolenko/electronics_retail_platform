from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
	openapi.Info(
		title="Electronic retail platform",
		default_version='v0.1',
		description="API для платформы торговой сети электроники",
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('admin/', admin.site.urls),
	path('', include('user.urls', namespace='user')),
	path('', include('shop.urls', namespace='shop')),
]
