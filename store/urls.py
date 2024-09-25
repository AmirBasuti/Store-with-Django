from django.urls import path

from store.views import *

urlpatterns = [
    path("products/", ProductList.as_view(), name='product-list'),
    path("products/<int:pk>/", ProductDetail.as_view(), name='product-detail'),
    path("collection/<int:pk>/", CollectionDetail.as_view(), name='collection-detail'),
    path("collection/", CollectionList.as_view(), name='collection-list'),
]