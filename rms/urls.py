from .views import *
from django.urls import path

urlpatterns = [
    
    # Category routes: 
    path('category/',category_list),
    path('category/<id>/',category_detail),
    
    # Food routes: 
    path('food/', food_list),
    path('food/<id>/', food_detail),
    
    
    # Table routes: 
    path('table/', table_list),
    path('table/<id>/', table_detail),
    
    # Order routes: 
    path('order/', order_list),
    path('order/<id>/', order_detail),
    
    # OrderItem routes: 
    path('order_item/', order_item_list),
    path('order_item/<id>/', order_item_detail),
]