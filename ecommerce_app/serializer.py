from rest_framework import serializers
from .models import Products

class products_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name','cost','description','image']
