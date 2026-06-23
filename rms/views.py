from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.


# Category API ------------------------------------------------------------------
class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        item = OrderItem.objects.filter(food__category = category).count()
        if item>0:
            return Response("Protected!", 400)
        
        category.delete()
        return Response("Deleted successfully!", 204)


# Food API ----------------------------------------------------------------------
class FoodAPI(viewsets.ModelViewSet):
    
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    def destroy(self, request, *args, **kwargs):
        food = self.get_object()
        item = OrderItem.objects.filter(food = food).count()
        if item >0:
            return Response("Protected! Related to OrderItem.", 400)
        
        food.delete()
        return Response("Food deleted", 204)
        

# Table API --------------------------------------------------------

class TableAPI(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        item = OrderItem.objects.filter(order__table = table).count()
        if item>0: 
            return Response("Protected! Related to Order in OrderItem.", 400)
        
        table.delete()
        return Response("Table deleted", 204)



# Order API -------------------------------------------------

class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        item = OrderItem.object.filter(order = order).count()
        if item > 0:
            return Reponse("Protected!. Related to OrderItem.", 400)
        
        order.delete()
        return Response("Order deleted. ", 204)


# OrderItem API -------------------------------------------------------

class OrderItemAPI(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


# User API ----------------------------------------------------------------

class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        item = OrderItem.objects.filter(order__user = user).count()
        if item > 0: 
            return Response("Protected! Related to Order of OrderItem.", 400)
        
        user.delete()
        return Response("User deleted.", 204)