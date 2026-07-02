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
    price_with_tax = serializers.SerializerMethodField()        # to put extra filed in the serializer 
    category_name = serializers.StringRelatedField(source = 'category')                 # to show names(string) instead of id of a FK model
    
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'category', 'category_name', 'price', 'price_with_tax']
        
    def get_price_with_tax(self, Food):             # method to calculate tax
        return Food.price * 0.10 + Food.price


# Table serializer 

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'      # '__all__' : includes all model fields into the serializer 
    


# OrderItem Serializer

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"
        

    
# Order Serializer

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())      # 'CurrentUserDefault()' : send the current logged-in user automatically, 'HiddenField' : hide the field from the serializer post
    user_name = serializers.StringRelatedField(source = 'user')
    items = OrderItemSerializer(many = True)      # it's necessay to include 'many=True' here because 'OrderItem' serializer serializes multiple data
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'table', 'total_price', 'status', 'payment_status', 'items']
    


# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
