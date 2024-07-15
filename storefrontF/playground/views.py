from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from store.models import Customer, Product, Collection, Promotion, Cart, Order, Adress, OrderItem
from django.db.models import Q, F, aggregates




def say_hello(request):
    object = Order.objects.select_related("customer").prefetch_related('orderitem_set__product').order_by('placed_at')[:5]
    # print(object)
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'object': object}, request))