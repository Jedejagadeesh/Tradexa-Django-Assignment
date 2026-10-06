from rest_framework import serializers
from .models import Product, Order, Box


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_length(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Length must be greater than 0."
            )
        return value

    def validate_width(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Width must be greater than 0."
            )
        return value

    def validate_height(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Height must be greater than 0."
            )
        return value

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Weight must be greater than 0."
            )
        return value


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = '__all__'

    def validate(self, data):
        if data['length'] <= 0:
            raise serializers.ValidationError(
                "Length must be greater than 0."
            )

        if data['width'] <= 0:
            raise serializers.ValidationError(
                "Width must be greater than 0."
            )

        if data['height'] <= 0:
            raise serializers.ValidationError(
                "Height must be greater than 0."
            )

        if data['max_weight'] <= 0:
            raise serializers.ValidationError(
                "Maximum weight must be greater than 0."
            )

        return data


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)

        instance.save()

        if products is not None:
            instance.products.set(products)

        return instance