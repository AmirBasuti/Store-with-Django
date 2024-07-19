from django.urls import path

from store.views import product_list, product_detail, collection_detail

urlpatterns = [
    path("products/", product_list, name='product-list'),
    path("products/<int:pk>/", product_detail, name='product-detail'),
    path("collection/<int:pk>/", collection_detail, name='collection-detail'),
]