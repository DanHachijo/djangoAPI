from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    phone = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name
    # auto_now_addはレコードの作成した日と時間のみ記録する
