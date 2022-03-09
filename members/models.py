from django.db import models


# class Country(models.Model):
#     name = models.CharField(max_length=30)

#     class Meta:
#         verbose_name_plural = '国'

#     def __str__(self):
#         return self.name


class Office(models.Model):
    # id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=30, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    suite = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)

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
    office = models.ForeignKey(Office, on_delete=models.PROTECT, related_name='office')
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