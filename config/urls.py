from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('user.urls', namespace='user')),
	path('', include('shop.urls', namespace='shop')),
]
