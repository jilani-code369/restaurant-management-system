from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema

from .models import *
from .serializers import *
from .pagination import *
from .filters import *


# Create your views here.


# Category API ------------------------------------------------------------------
@extend_schema(tags=['Category'])              # implement extend_schema tags for Swagger grouping
class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #Permission:
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #Pagination: 
    pagination_class = PageOfTen                     # pagination class of ten data 
    
    #Filtering:
    filter_backends = [SearchFilter]
    search_fields = ['name']
    
    #Overriding destroy method:
    def destroy(self, request, *args, **kwargs):       # overriding destroy method to handle protected relationship 
        category = self.get_object()
        item = OrderItem.objects.filter(food__category = category).count()
        if item>0:
            return Response("Protected!", 400)
        
        category.delete()
        return Response("Deleted successfully!", 204)


# Food API ----------------------------------------------------------------------

@extend_schema(tags=['Food'])
class FoodAPI(viewsets.ModelViewSet):
    queryset = Food.objects.select_related('category').all()
    serializer_class = FoodSerializer
    
    #Permission
    permission_classes = [IsAuthenticated]
    
    #Pagination:
    pagination_class = PageOfTwenty                      # pagination class of twenty data
    
    #Filtering:
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'category__name']           # '__name' is used to lookup text field inside fk relationship because SearchFilter require text field to perform search
    filterset_class = FoodFilter
    ordering_fields = ['price']
    
         
    def destroy(self, request, *args, **kwargs):
        food = self.get_object()
        item = OrderItem.objects.filter(food = food).count()
        if item >0:
            return Response("Protected! Related to OrderItem.", 400)
        
        food.delete()
        return Response("Food deleted", 204)
        

# Table API --------------------------------------------------------

@extend_schema(tags=['Table'])
class TableAPI(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    #Permission
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #Pagination: 
    pagination_class = PageOfTen
    
    #Filtering: 
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['table_number']
    ordering_fields = ['capacity']
    
    
    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        item = OrderItem.objects.filter(order__table = table).count()
        if item>0: 
            return Response("Protected! Related to Order in OrderItem.", 400)
        
        table.delete()
        return Response("Table deleted", 204)



# Order API -------------------------------------------------

@extend_schema(tags=['Order'])
class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items').all()
    serializer_class = OrderSerializer
    
    #Permission
    permission_classes = [IsAuthenticated]
    
    #Pagination:
    pagination_class = PageOfTwenty
    
    #Filtering:
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'table', 'status']
    
    
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        item = OrderItem.objects.filter(order = order).count()
        if item > 0:
            return Reponse("Protected!. Related to OrderItem.", 400)
        
        order.delete()
        return Response("Order deleted. ", 204)


# OrderItem API -------------------------------------------------------

@extend_schema(tags=['OrderItem'])
class OrderItemAPI(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    #Permission
    permission_classes = [IsAuthenticated]
    
    #Pagination: 
    pagination_class = PageOfTen
    
    #Filtering:
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['order__user__username', 'food__name', 'order__table__table_number']
    filterset_fields = ['food', 'order', 'order__table']


# User API ----------------------------------------------------------------

@extend_schema(tags=['User'])
class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #Permission
    permission_classes = [AllowAny]
    
    #Pagination: 
    pagination_class = PageOfTen
    
    #Filtering:
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username']
    
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        item = OrderItem.objects.filter(order__user = user).count()
        if item > 0: 
            return Response("Protected! Related to Order of OrderItem.", 400)
        
        user.delete()
        return Response("User deleted.", 204)