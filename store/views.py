# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


# Create your views here.
@api_view()
def product_list(request):
    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
