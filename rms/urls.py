from .views import *
from django.urls import path

urlpatterns = [
    
    # Category routes: 
    path('category/', CategoryAPI.as_view({'get':'list', 'post' : 'create'})),
    path('category/<pk>/', CategoryAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
    # Food routes: 
    path('food/', FoodAPI.as_view({'get':'list', 'post':'create'})),
    path('food/<pk>/', FoodAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
    
    # Table routes: 
    path('table/', TableAPI.as_view({'get':'list', 'post':'create'})),
    path('table/<pk>/', TableAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
    
    # Order routes: 
    path('order/', OrderAPI.as_view({'get':'list', 'post':'create'})),
    path('order/<pk>/', OrderAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
    
    # OrderItem routes: 
    path('order-item/', OrderItemAPI.as_view({'get':'list', 'post':'create'})),
    path('order-item/<pk>/', OrderItemAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
    
    # User routes:path('order/', OrderView.as_view()),
    path('user/', UserAPI.as_view({'get':'list', 'post':'create'})),
    path('user/<pk>/', UserAPI.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    
]