from itertools import product

from django.urls import path, include

from store.views import *
# from rest_framework import routers
from rest_framework_nested import routers
router = routers.DefaultRouter() # Simplerouter
router.register('products', ProductViewSet, basename='products')
router.register('collection', CollectionViewSet)
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', viewset= ReviewViewSet, basename='product-reviews')
# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = router.urls + product_router.urls
# urlpatterns = [
#     path("products/", ProductList.as_view(), name='product-list'),
#     path("products/<int:pk>/", ProductDetail.as_view(), name='product-detail'),
#     path("collection/<int:pk>/", CollectionDetail.as_view(), name='collection-detail'),
#     path("collection/", CollectionList.as_view(), name='collection-list'),
# ]