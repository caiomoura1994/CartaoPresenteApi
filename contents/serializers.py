from rest_framework import serializers

from .models import Product, Order, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            'original',
            'medium',
            'small',
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'is_active',
            'price',
            'stock',
            'images',
            'id',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
