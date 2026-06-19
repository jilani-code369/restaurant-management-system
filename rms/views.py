from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


# Category API ------------------------------------------------------------------

## get, post:
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



## get, put, patch, delete:
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
    
    def patch(self, request,id):        # patch: partially updates the fields (all fields are not required) in the payload
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data = request.data, partial=True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request,id):
        category = Category.objects.get(id = id)
        item = OrderItem.objects.filter(food__category = category).count()
        if item >0:
            return Response("Protected: Category cannot be deleted. Related to Food in OrderItem.", 400)
        
        category.delete()
        return Response("Data deleted successfully", status.HTTP_204_NO_CONTENT)
    


# Food API ----------------------------------------------------------------------

## get, post:
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


## get, put, patch, delete: 
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
        food = Food.objects.get(id=id)
        item = OrderItem.objects.filter(food = food ).count()
        if item > 0:
            return Response("Protected: Food cannot be deleted. Related to OrderItem.", 400)
        
        food.delete()
        return Response("Deleted successfully", 204)
    


# Table API --------------------------------------------------------

## get,post: 
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


## get, put, patch, delete:

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
        table = Table.objects.get(id=id)
        item = OrderItem.objects.filter(order__table = table)
        if item > 0:
            return Response("Protected: Table cannot be delete. Related to Order in OrderItem.", 400)
        
        return Response("Deleted successfully", 204)
    
    

# Order API -------------------------------------------------

## get, post: 
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


## get, put, patch, delete: 
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
        order = Order.objects.get(id=id)
        item = OrderItem.objects.filter(order = order).count()
        if item > 0:
            return Response("Protected: Order cannot be deleted. Related to OrderItem.", 400)
        
        order.delete()
        return Response("Deleted successfully", 204)
    
    
    
# OrderItem API -------------------------------------------------------

## get, post: 
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


## get, put, patch, delete: 
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



# User API: ----------------------------------------

## get, post: 
class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, 201)
    
    
## get, put, patch, delete: 
class UserDetail(APIView):
    def get(self, request, id):
        user = User.objects.get(id = id)
        serializer = UserSerializer(user)
    
        return Response(serializer.data)
    
    def put(self, request, id):
        user = User.objects.get(id = id )
        serializer = UserSerializer(user, data= request.data)
        serializer.is_valid()
        serializer.save()
        
        return Response(serializer.data, 201)
    
    def patch(self, request, id):
        user = User.objects.get(id = id )
        serializer = UserSerializer(user, data= request.data, partial = True)
        serializer.is_valid()
        serializer.save()
        
        return Response(serializer.data, 201)
    
    def delete(self, request, id):
        user = User.objects.get(id = id )
        item = OrderItem.objects.filter(order__user = user).count()
        if item > 0:
            return Response("Protected: Cannot be deleted. Related or Order in OrderItem.", 400)
        
        user.delete()
        return Response("User deleted successfully.", 204)
    
    