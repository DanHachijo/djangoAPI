from django.db import models
# Importing the Member model and customers models
from members.models import Member
from customers.models import Store


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category_name")
    staff = models.ForeignKey(Member, on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    # urgent = models.BooleanField(default=False, blank=False)
    status = models.BooleanField(default=False)
    inquiry = models.CharField(max_length=1000)
    respond = models.CharField(max_length=1000)
    # Custromer Info
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    contact_name = models.CharField(max_length=100, default="Staff")
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    escalated = models.BooleanField(default=False, blank=False)

    class Meta:
        verbose_name_plural = 'チケット'
        # ordering = ('date')

    def __str__(self):
        return self.inquiry
