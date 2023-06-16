from django.shortcuts import render
from price.models import PriceTable, PriceCard


def first_page(request):
    return render(request,
                  'index.html',
                  {
                      'objects_price_table': PriceTable.objects.all(),
                      'bronze_price': PriceCard.objects.get(pk=1),
                      'silver_price': PriceCard.objects.get(pk=2),
                      'gold_price': PriceCard.objects.get(pk=3),
                  })
