import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = {'collection_id': ['exact'],
                  'unit_price': ['lt', 'gt']}