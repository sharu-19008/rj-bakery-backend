from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price', 'category','food_type', 'is_available','average_rating', 'total_no_of_ratings','image' ]