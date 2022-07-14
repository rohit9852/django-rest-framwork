from csv import field_size_limit
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(allow_null=True, max_length=None, allow_empty_file=False, required=False)
    class Meta:
        model = Product
        fields= ('id', 'name', 'description', 'category', 'price', 'image')