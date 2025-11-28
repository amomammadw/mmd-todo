from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from apps.user.models import User
from apps.user.serializers import UserCreateSerializer, UserSerializer


# Create your views here.
class UserViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = User.objects.all()
    serializer_class = UserSerializer
