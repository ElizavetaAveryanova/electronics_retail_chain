from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """API View для создания нового пользователя."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """"Сохранение нового пользователя после валидации."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()