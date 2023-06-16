from django.db import models


class PriceCard(models.Model):
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.price}'


class PriceTable(models.Model):
    services = models.CharField(max_length=200)
    new_price = models.CharField(max_length=200)
    old_price = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.services}'
