from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


# Category API ------------------------------------------------------------------
class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)  # serialization : object converted into json
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data = request.data)   # deserialization : json converted into object
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)




class CategoryDetail(APIView):
    def get(self, request,id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request,id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request,id):
        category = Category.objects.get(id = id)
        category.delete()
        
        return Response("Data deleted successfully", status.HTTP_204_NO_CONTENT)
    


# Food API ----------------------------------------------------------------------


class FoodView(APIView):
    def get(self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = FoodSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


class FoodDetail(APIView):
    def get(self, request, id):
        food = Food.objects.get(id = id)
        serializer = FoodSerializer(food)
        
        return Response(serializer.data, 200)
    
    def put(self, request, id):
        food = Food.objects.get(id=id)
        serializer = FoodSerializer(food, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    def patch(self, request, id):
        food = Food.objects.get(id=id)
        serializer = FoodSerializer(food, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    def delete(self, request, id):
        Food.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    


# Table API --------------------------------------------------------

class TableView(APIView):
    def get(self, request):
        food = Table.objects.all()
        serializer = TableSerializer(food, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TableSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)



class TableDetail(APIView):
    def get(self, request, id):
        food = Table.objects.get(id = id)
        serializer = TableSerializer(food)
        
        return Response(serializer.data, 200)
    
    def put(self, request, id):
        food = Table.objects.get(id=id)
        serializer = TableSerializer(food, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    def patch(self, request, id):
        food = Table.objects.get(id=id)
        serializer = TableSerializer(food, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    def delete(self, request, id):
        Table.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    
    

# Order API -------------------------------------------------

class OrderView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


class OrderDetail(APIView):
    def get(self, request, id):
        order = Order.objects.get(id = id)
        serializer = OrderSerializer(order)
        
        return Response(serializer.data, 200)
    
    def put(self, request, id):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    def patch(self, request, id):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    def delete(self, request, id):
        Order.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    
    
    
# OrderItem API -------------------------------------------------------


class OrderItemView(APIView):
    def get(self, request):
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many = True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrderItemSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)


class OrderItemDetail(APIView):
    def get(self, request, id):
        order_item = OrderItem.objects.get(id = id)
        serializer = OrderItemSerializer(order_item)
        
        return Response(serializer.data, 200)
    
    def put(self, request, id):
        order_item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(order_item, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    def patch(self, request, id):
        order_item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(order_item, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
    def delete(self, request, id):
        OrderItem.objects.get(id=id).delete()
        
        return Response("Deleted successfully", 204)
    