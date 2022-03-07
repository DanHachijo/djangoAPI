from .models import Store
from .serializers import StoreSerializer
from rest_framework import viewsets


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Store.objects.filter(status="Active")
    serializer_class = StoreSerializer
