from django.db import models


class Order(models.Model):
    datatime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    phone = models.CharField(max_length=200, verbose_name='Phone')

    def __str__(self):
        return f"{self.name} {self.phone}"
