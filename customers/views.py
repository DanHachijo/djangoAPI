from .models import Store
from .serializers import StoreSerializer
from rest_framework import viewsets

class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    # これを追加
    # これを追加

    queryset = Store.objects.filter(status="Active")
    # queryset = Member.objects.all()
    serializer_class = StoreSerializer
