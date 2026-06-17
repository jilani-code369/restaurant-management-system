from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from .models import *
from .serializers import *

# Create your views here.


# Category API ------------------------------------------------------------------

## GET, POST: 
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)  # serialization : object converted into json
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data = request.data)   # deserialization : json converted into object
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


## GET (with id), PUT, DELETE: 

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        category = Category.objects.get(id = id)
        category.delete()
        
        return Response("Data deleted successfully", status.HTTP_204_NO_CONTENT)
    


# Food API ----------------------------------------------------------------------


## GET, POST: 
@api_view(['GET', 'POST'])
def food_list(request):
    if request.method == 'GET':
        food = Food.objects.all()
        serializer = FoodSerializer(food, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = FoodSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


## GET(with id), PUT, PATCH, DELETE:

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def food_detail(request, id):
    if request.method == 'GET':
        food = Food.objects.get(id = id)
        serializer = FoodSerializer(food)
        
        return Response(serializer.data, 200)
    
    elif request.method == 'PUT':
        food = Food.objects.get(id=id)
        serializer = FoodSerializer(food, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    elif request.method == 'PATCH':
        food = Food.objects.get(id=id)
        serializer = FoodSerializer(food, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    elif request.method == 'DELETE':
        Food.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    


# Table API --------------------------------------------------------

## GET, POST: 
@api_view(['GET', 'POST'])
def table_list(request):
    if request.method == 'GET':
        food = Table.objects.all()
        serializer = TableSerializer(food, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TableSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


## GET(with id), PUT, PATCH, DELETE:
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def table_detail(request, id):
    if request.method == 'GET':
        food = Table.objects.get(id = id)
        serializer = TableSerializer(food)
        
        return Response(serializer.data, 200)
    
    elif request.method == 'PUT':
        food = Table.objects.get(id=id)
        serializer = TableSerializer(food, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    elif request.method == 'PATCH':
        food = Table.objects.get(id=id)
        serializer = TableSerializer(food, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    elif request.method == 'DELETE':
        Table.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    
    

# Order API -------------------------------------------------

## GET, POST: 
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


## GET(with id), PUT, PATCH, DELETE:

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def order_detail(request, id):
    if request.method == 'GET':
        order = Order.objects.get(id = id)
        serializer = OrderSerializer(order)
        
        return Response(serializer.data, 200)
    
    elif request.method == 'PUT':
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    elif request.method == 'PATCH':
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    elif request.method == 'DELETE':
        Order.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    
    
    
# OrderItem API -------------------------------------------------------


## GET, POST: 
@api_view(['GET', 'POST'])
def order_item_list(request):
    if request.method == 'GET':
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = OrderItemSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


## GET(with id), PUT, PATCH, DELETE:

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def order_item_detail(request, id):
    if request.method == 'GET':
        order_item = OrderItem.objects.get(id = id)
        serializer = OrderItemSerializer(order_item)
        
        return Response(serializer.data, 200)
    
    elif request.method == 'PUT':
        order_item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(order_item, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    elif request.method == 'PATCH':
        order_item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(order_item, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    elif request.method == 'DELETE':
        OrderItem.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    