from rest_framework import serializers
from .models import *
from rest_framework.response import Response


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
    
    
# Food Serializer
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'category']

    
# Table serializer 

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'      # '__all__' : includes all model fields into the serializer 
    
    
# Order Serializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['total_price']     # 'exclude': exclude specific fields form input/output in serializer
    
    
# OrderItem Serializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        

