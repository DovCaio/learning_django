from rest_framework import serializers
from products.models import Product

class ProductSerializerMinimized(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "brand", "price"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"