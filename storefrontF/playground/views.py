from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.template import loader
from store.models import Product, Collection, Cart, CartItem
from tags.models import TaggedItem


def say_hello(request):
    # resualt = Order.objects.aggregate(count = Count(id)) resualt = OrderItem.objects.filter(product_id=
    # 1).aggregate(count = Sum('quantity')) resualt = Order.objects.filter(customer_id= 1).aggregate(count = Count(
    # 'id')) resualt = Product.objects.filter(collection__id= 3).aggregate(Min = Min('unit_price'), Max = Max(
    # 'unit_price'), Avg = Avg('unit_price')) resualt = Customer.objects.annotate(last_order_id = Max('order__id'))
    # resualt = Collection.objects.annotate(count = Count('product__id')) resualt = Customer.objects.annotate(count =
    # Count('order__id')).filter(count__gt=5) a = Order.objects.annotate(total = Sum('orderitem__unit_price'))
    # resualt = Customer.objects.annotate(total =Sum(F('order__orderitem__unit_price')) * F(
    # 'order__orderitem__quantity')) resualt = Product.objects.annotate(total = Sum(F('orderitem__unit_price') * F(
    # 'orderitem__quantity'))).order_by('-total')[:5]
    # content_type = ContentType.objects.get_for_model(Product)
    # resualt = TaggedItem.objects.select_related('tag').filter(content_type= content_type, object_id=1)
    # resualt = TaggedItem.objects.get_tags_for(Product, 1)
    # collection  = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # cart = Cart()
    # cart.save()
    mio = CartItem.objects.get(pk=2)

    mio.cart = cart
    mio.product = Product(pk=1)
    mio.quantity = 2
    mio.save()

    mio.quantity = 3
    mio.save()

    mio.delete()
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({'resualt': resualt}, request))
