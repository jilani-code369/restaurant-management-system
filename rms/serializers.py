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
    category = serializers.StringRelatedField()                 # to show names(string) instead of id of a FK model
    category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())  # to show id of a FK mdoel
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'price_with_tax', 'category_id', 'category']
        
    def get_price_with_tax(self, Food):             # method to calculate tax
        return Food.price * 0.10 + Food.price


# Table serializer 

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'      # '__all__' : includes all model fields into the serializer 
    
   
    
# Order Serializer

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    table = serializers.StringRelatedField()
    table_id = serializers.PrimaryKeyRelatedField(queryset = Table.objects.all())
    
    class Meta:
        model = Order
        exclude = ['total_price']     # 'exclude': exclude specific fields form input/output in serializer
    
    
# OrderItem Serializer

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()
    order_id = serializers.PrimaryKeyRelatedField(queryset= Order.objects.all())
    food = serializers.StringRelatedField()
    food_id = serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())
    
    class Meta:
        model = OrderItem
        fields = "__all__"
        

# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
