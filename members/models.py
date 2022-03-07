from django.db import models


# class Country(models.Model):
#     name = models.CharField(max_length=30)

#     class Meta:
#         verbose_name_plural = '国'

#     def __str__(self):
#         return self.name


class Office(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    zip = models.IntegerField()

    class Meta:
        verbose_name_plural = 'オフィス'

    def __str__(self):
        return self.name


class Member(models.Model):
    EMPOLYMENT_STATUS = [
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
    ]

    name = models.CharField(max_length=50, null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.PROTECT)
    email = models.EmailField(max_length=60, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=EMPOLYMENT_STATUS, default="Active",)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'スタッフ'

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} | {self.office.name}"

    def __str__(self):
        return self.name