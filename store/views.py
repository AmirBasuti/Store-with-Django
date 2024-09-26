# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from store.models import Product, Collection
from store.serializers import ProductSerializer, CollectionSerializer



# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()

    serializer_class = ProductSerializer
    # def get_serializer_class(self):
    #     return ProductSerializer

    def get_serializer_context(self):
        return {'request':self.request}
    #
    # def get(self, request:Request):
    #     queryset = Product.objects.select_related('collection').all()
    #     serializer = ProductSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def post(self, request:Request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request:Request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    def put(self, request:Request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request:Request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.exists():
            return Response({'error': 'Product cannot be deleted because it is associated with an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):
    def get(self, request:Request):
        queryset = Collection.objects.prefetch_related('products').all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def post(self, request:Request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class CollectionDetail(APIView):
    def get(self, request:Request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request:Request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Response(serializer.data, status= status.HTTP_202_ACCEPTED)

    def delete(self, request:Request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.exists():
            return Response({'error': 'Collection cannot be deleted because it is associated with a product'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
