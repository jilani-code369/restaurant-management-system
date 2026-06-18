from .views import *
from django.urls import path

urlpatterns = [
    
    # Category routes: 
    path('category/', CategoryView.as_view()),
    path('category/<id>/', CategoryDetail.as_view()),
    
    # Food routes: 
    path('food/', FoodView.as_view()),
    path('food/<id>/', FoodDetail.as_view()),
    
    
    # Table routes: 
    path('table/', TableView.as_view()),
    path('table/<id>/', TableDetail.as_view()),
    
    # Order routes: 
    path('order/', OrderView.as_view()),
    path('order/<id>/', OrderDetail.as_view()),
    
    # OrderItem routes: 
    path('order_item/', OrderItemView.as_view()),
    path('order_item/<id>/', OrderItemDetail.as_view()),
]