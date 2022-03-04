from django.contrib import admin
from .models import Store

members = [Store]
admin.site.register(members)
# Register your models here.
