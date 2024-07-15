from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Customer, Product, Collection, Promotion, Cart, Order, Adress, OrderItem





def say_hello(request):

    # resualt = Order.objects.aggregate(count = Count(id))
    # resualt = OrderItem.objects.filter(product_id= 1).aggregate(count = Sum('quantity'))
    # resualt = Order.objects.filter(customer_id= 1).aggregate(count = Count('id'))
    # resualt = Product.objects.filter(collection__id= 3).aggregate(Min = Min('unit_price'), Max = Max('unit_price'), Avg = Avg('unit_price'))
    # resualt = Customer.objects.annotate(last_order_id = Max('order__id'))
    # resualt = Collection.objects.annotate(count = Count('product__id'))
    # resualt = Customer.objects.annotate(count = Count('order__id')).filter(count__gt=5)
    # a = Order.objects.annotate(total = Sum('orderitem__unit_price'))
    # resualt = Customer.objects.annotate(total =Sum(F('order__orderitem__unit_price')) * F('order__orderitem__quantity'))
    resualt = Product.objects.annotate(total = Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total')[:5]
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'resualt': resualt}, request))