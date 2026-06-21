from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import *

from .models import *
from .serializers import *

# Create your views here.


# Category API ------------------------------------------------------------------

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        item = OrderItem.objects.filter(food__category = category).count()
        if item >0:
            return Response("Protected: Category cannot be deleted. Related to Food in OrderItem.", 400)
        
        category.delete()
        return Response("Data deleted successfully", status.HTTP_204_NO_CONTENT)
    


# Food API ----------------------------------------------------------------------


class FoodView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodDetail(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    def delete(self, request, *args, **kwargs):
        food = self.get_object()
        item = OrderItem.objects.filter(food = food).count()
        if item >0:
            return Response("Protected! Related to OrderItem.", 400)
        
        food.delete()
        return Response("Food deleted", 204)
        

# Table API --------------------------------------------------------

class TableView(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
class TableDetail(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    def delete(self, request, *args, **kwargs):
        table = self.get_object()
        item = OrderItem.objects.filter(order__table = table).count()
        if item>0: 
            return Response("Protected! Related to Order in OrderItem.", 400)
        
        table.delete()
        return Response("Table deleted", 204)



# Order API -------------------------------------------------

class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def delete(self, request, *args, **kwargs):
        order = self.get_object()
        item = OrderItem.object.filter(order = order).count()
        if item > 0:
            return Reponse("Protected!. Related to OrderItem.", 400)
        
        order.delete()
        return Response("Order deleted. ", 204)


# OrderItem API -------------------------------------------------------

class OrderItemView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    


# User API ----------------------------------------------------------------

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        item = OrderItem.objects.filter(order__user = user).count()
        if item > 0: 
            return Respnse("Protected! Related to Order of OrderItem.", 400)
        
        user.delete()
        return Response("User deleted.", 204)