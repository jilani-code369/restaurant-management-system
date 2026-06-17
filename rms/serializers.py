from rest_framework import serializers
from .models import *
from rest_framework.response import Response


# Category Serializer

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()

    # Custom create() method: 
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        
        return category
    
    # Custom update() method: 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        
        return instance
    
    
# Food Serializer

class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), allow_null=True)
    
    # Custom create() method: 
    def create(self, validated_data):
        food = Food.objects.create(**validated_data)
        
        return food
    
    # Custom update() method:
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        
        instance.save()
        
        return instance
    
    
    
# Table serializer 

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    table_number = serializers.CharField()  
    capacity = serializers.IntegerField()
    available = serializers.BooleanField(required = False)
    
    
    # Custom create() method: 
    def create(self, validated_data):
        table = Table.objects.create(**validated_data)
        
        return table
    
    # Custom update() method:
    def update(self, instance, validated_data):
        instance.table_number = validated_data.get('table_number', instance.table_number)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.available = validated_data.get('available', instance.available)
        
        instance.save()
        
        return instance
    
    
    
# Order Serializer

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), allow_null = True)
    table = serializers.PrimaryKeyRelatedField(queryset = Table.objects.all(), allow_null = True)
    total_price = serializers.FloatField()
    status = serializers.ChoiceField(choices = Order.STATUS_CHOICES, required = False)
    payment_status = serializers.BooleanField(required = False)
    
    # Custom create() method: 
    def create(self, validated_data):
        table = Order.objects.create(**validated_data)
        
        return table
    
    # Custom update() method:
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.table = validated_data.get('table', instance.table)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        
        instance.save()
        
        return instance
    
    
# OrderItem Serializer

class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    order = serializers.PrimaryKeyRelatedField(queryset = Order.objects.all())
    food = serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())

    
    # Custom create() method: 
    def create(self, validated_data):
        table = OrderItem.objects.create(**validated_data)
        
        return table
    
    # Custom update() method:
    def update(self, instance, validated_data):
        instance.order = validated_data.get('order', instance.order)
        instance.food = validated_data.get('food', instance.food)

        
        instance.save()
        
        return instance