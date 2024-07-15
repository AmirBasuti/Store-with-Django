from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from store.models import Customer, Product, Collection, Promotion, Cart, Order, Adress
from django.db.models import Q




def say_hello(request):
    # object = Product.objects.filter(unit_price__gt=20.0).order_by('title')
    # object = Customer.objects.filter(email__icontains='.com')
    # object = Collection.objects.filter(featured_product__isnull=True)
    # object = Product.objects.filter(inventory__lt=10)
    # object = Order.objects.filter(customer_id=1)
    # print(object)
    object = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20.0))
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'object': object}, request))