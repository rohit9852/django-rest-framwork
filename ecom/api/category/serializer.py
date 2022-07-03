from csv import field_size_limit
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields= ('name', 'description')