from django.contrib import admin
from .models import Category, Ticket

tickets = [Category, Ticket]
admin.site.register(tickets)

