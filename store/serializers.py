from decimal import Decimal

from rest_framework import serializers

from store.models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'featured_product']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='cal_price_with_tax')

    @staticmethod
    def cal_price_with_tax(product):
        return round(product.unit_price * Decimal(1.1), 2)
