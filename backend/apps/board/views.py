from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
)

from apps.board.models import Board
from apps.board.serializers import BoardCreateSerializer, BoardSerializer


class BoardPagination(LimitOffsetPagination):
    default_limit = 15


# Create your views here.
class BoardViewSet(
    GenericViewSet,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
):
    http_method_names = ["get", "post", "put", "delete"]
    pagination_class = BoardPagination

    def get_serializer_class(self):
        if self.action == "create":
            return BoardCreateSerializer
        else:
            return BoardSerializer

    def get_queryset(self):
        return Board.objects.all()
