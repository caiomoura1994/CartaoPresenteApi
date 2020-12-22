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


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
