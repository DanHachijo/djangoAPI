from django.contrib import admin
from .models import Company, Store

members = [Company, Store]
admin.site.register(members)
# Register your models here.
