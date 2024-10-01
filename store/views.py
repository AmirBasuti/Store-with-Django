# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Collection, OrderItem, Review
from .serializers import *


# Create your views here.
class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


    def destroy(self, request, *args, **kwargs):

        if OrderItem.objects.filter(product_id=kwargs["pk"]).exists():
            return Response({'error': 'Product cannot be deleted because it is associated with an order item'},
                                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    # def destroy(self, request: Request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     if product.orderitems.exists():
    #         return Response({'error': 'Product cannot be deleted because it is associated with an order item'},
    #                         status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()

#
# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.select_related.all()
#
#     serializer_class = ProductSerializer
#
#     def get_serializer_context(self):
#         return {'request':self.request}
#
#
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_serializer_context(self):
#         return {'request':self.request}
#
#     def delete(self, request: Request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.orderitems.exists():
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item'},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.prefetch_related('products').all()
    serializer_class = CollectionSerializer
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['PK']).exists():
            return Response({'error': 'Collection cannot be deleted because it is associated with a product'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)

    # def delete(self, request:Request, pk):
    #     collection = get_object_or_404(Collection, pk=pk)
    #     if collection.products.exists():
    #         return Response({'error': 'Collection cannot be deleted because it is associated with a product'},
    #                         status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.prefetch_related('products').all()
#     serializer_class = CollectionSerializer
#
# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#
#     def delete(self, request:Request, pk):
#         collection = get_object_or_404(Collection, pk=pk)
#         if collection.products.exists():
#             return Response({'error': 'Collection cannot be deleted because it is associated with a product'},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(ModelViewSet):
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    # queryset = Review.objects.all()
    serializer_class = ReviewSerilizer
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}

