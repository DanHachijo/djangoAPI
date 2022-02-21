from django.contrib import admin
from .models import Member, Office, Country

members = [Member, Office, Country]
admin.site.register(members)
