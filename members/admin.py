from django.contrib import admin
from .models import Member, Office

members = [Member, Office]
admin.site.register(members)
