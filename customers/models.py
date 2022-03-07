from django.db import models

# class Company(models.Model):
#     COMPANY_STATUS = [
#         ('Active', 'Active'),
#         ('Pending', 'Pending'),
#         ('Lost', 'Lost'),
#     ]
#     name = models.CharField(max_length=30)
#     street = models.CharField(max_length=100)
#     suite = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     State = models.CharField(max_length=100)
#     zipcode = models.IntegerField()
#     status = models.CharField(
#         max_length=30, choices=COMPANY_STATUS, default="Active")

#     contact = models.CharField(max_length=30, blank=True, null=True)
#     phone = models.IntegerField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = '企業名'

#     def __str__(self):
#         return self.name


class Store(models.Model):
    COMPANY_STATUS = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Lost', 'Lost'),
    ]
    # company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, null=True, blank=True)
    street = models.CharField(max_length=100)
    status = models.CharField(
        max_length=30, choices=COMPANY_STATUS, default="Active")

    # contact = models.CharField(max_length=30, blank=True, null=True)
    # phone = models.IntegerField(blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '店舗名'

    def __str__(self):
        return f"{self.name} "
