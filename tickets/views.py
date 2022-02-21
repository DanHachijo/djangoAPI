# from msilib.schema import ServiceInstall
from tickets.models import Ticket, Category
from .serializers import TicketSerializer, CategorySerializer
from rest_framework import viewsets

class TicketViewSet(viewsets.ModelViewSet):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer