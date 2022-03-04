# from msilib.schema import ServiceInstall
from tickets.models import Ticket, Category
from .serializers import TicketSerializer, CategorySerializer
from rest_framework import viewsets
# from rest_framework.renderers import TemplateHTMLRenderer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-date')
    serializer_class = TicketSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
