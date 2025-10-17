from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
)
from apps.todo.models import Todo
from apps.todo.serializers import (
    TodoCreateSerializer,
    TodoSerializer,
    TodoUpdateSerializer,
)


class TodoPagination(LimitOffsetPagination):
    default_limit = 5


class TodoViewSet(
    GenericViewSet,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
):
    pagination_class = TodoPagination
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        return Todo.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return TodoCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return TodoUpdateSerializer
        else:
            return TodoSerializer
