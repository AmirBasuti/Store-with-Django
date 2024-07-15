from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, F
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Customer, Product, Collection, Promotion, Cart, Order, Adress, OrderItem





def say_hello(request):

    # resualt = Order.objects.aggregate(count = Count(id))
    # resualt = OrderItem.objects.filter(product_id= 1).aggregate(count = Sum('quantity'))
    # resualt = Order.objects.filter(customer_id= 1).aggregate(count = Count('id'))
    resualt = Product.objects.filter(collection__id= 3).aggregate(Min = Min('unit_price'), Max = Max('unit_price'), Avg = Avg('unit_price'))
    print(resualt)
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'resualt': resualt}, request))