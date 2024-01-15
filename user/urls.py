from django.urls import path

from user.apps import UserConfig

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from user.views import UserRegistrationAPIView

app_name = UserConfig.name


urlpatterns = [
	path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('register/', UserRegistrationAPIView.as_view(), name='register_user'),
]
