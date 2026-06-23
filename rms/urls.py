from .views import *
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()

router.register('category', CategoryAPI)
router.register('food', FoodAPI)
router.register('table', TableAPI)
router.register('order', OrderAPI)
router.register('order-item', OrderItemAPI)
router.register('user', UserAPI)




urlpatterns = [
    
] + router.urls