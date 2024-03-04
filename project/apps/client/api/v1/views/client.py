from rest_framework import permissions, viewsets

from apps.client.api.v1.filters.client import ClientCategoryFilterSet
from apps.client.api.v1.serializers.client import ClientCategorySerializer
from apps.client.models.client import ClientCategory


class ClientCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClientCategory.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ClientCategorySerializer
    filterset_class = ClientCategoryFilterSet
