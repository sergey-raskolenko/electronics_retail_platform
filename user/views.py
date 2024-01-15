from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserRegisterSerializer


class UserRegistrationAPIView(CreateAPIView):
	queryset = User.objects.all()
	permission_classes = [AllowAny]
	serializer_class = UserRegisterSerializer
