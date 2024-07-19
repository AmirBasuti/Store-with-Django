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
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='cal_price_with_tax')

    @staticmethod
    def cal_price_with_tax(product):
        return round(product.unit_price * Decimal(1.1), 2)

    #override the validate method
    # def validat(self, data):
    #     if data['password'] != data['password_confirm']:
    #         raise serializers.ValidationError('Passwords do not match')
    #

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other_field = 'other value'
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance