from decimal import Decimal

from rest_framework import serializers

from store.models import Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='cal_price_with_tax')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    collection = serializers.HyperlinkedRelatedField(
        view_name='collection-detail', read_only=True)
    def cal_price_with_tax(self, product):
        return round(product.unit_price * Decimal(1.1), 2)
