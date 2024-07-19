from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
