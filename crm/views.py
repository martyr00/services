from django.shortcuts import render
from price.models import PriceTable, PriceCard
from .forms import OrderForm
from .models import Order
from cms.models import CmsSlider
from telebot.send_message import sendTelegram


def first_page(request):
    return render(request, 'index.html',
                  {
                      'slider_list': CmsSlider.objects.all(),
                      'form': OrderForm(),
                      'objects_price_table': PriceTable.objects.all(),
                      'bronze_price': PriceCard.objects.get(pk=1),
                      'silver_price': PriceCard.objects.get(pk=2),
                      'gold_price': PriceCard.objects.get(pk=3),
                  })


def thx_page(request):

    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']

        Order(name=name, phone=phone).save()

        sendTelegram(name, phone)

        return render(request, './thanks.html', {'name': name})
    else:
        return render(request, './thanks.html')
