from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')

    def __str__(self):
        return f"{self.order_name} {self.order_phone}"
