from .views import *
from django.urls import path

urlpatterns = [
    
    # Category routes: 
    path('category/', CategoryView.as_view()),
    path('category/<pk>/', CategoryDetail.as_view()),
    
    # Food routes: 
    path('food/', FoodView.as_view()),
    path('food/<pk>/', FoodDetail.as_view()),
    
    
    # Table routes: 
    path('table/', TableView.as_view()),
    path('table/<pk>/', TableDetail.as_view()),
    
    # Order routes: 
    path('order/', OrderView.as_view()),
    path('order/<pk>/', OrderDetail.as_view()),
    
    # OrderItem routes: 
    path('order-item/', OrderItemView.as_view()),
    path('order-item/<pk>/', OrderItemDetail.as_view()),
    
    # User routes:path('order/', OrderView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<pk>/', UserDetail.as_view()),
]