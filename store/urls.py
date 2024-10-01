from django.urls import path, include

from store.views import *
from rest_framework import routers

router = routers.DefaultRouter() # Simplerouter
router.register('products', ProductViewSet)
router.register('collection', CollectionViewSet)
# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = router.urls
# urlpatterns = [
#     path("products/", ProductList.as_view(), name='product-list'),
#     path("products/<int:pk>/", ProductDetail.as_view(), name='product-detail'),
#     path("collection/<int:pk>/", CollectionDetail.as_view(), name='collection-detail'),
#     path("collection/", CollectionList.as_view(), name='collection-list'),
# ]