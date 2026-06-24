from .views import *
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()      # 'DefaultRouter' creates url links of APIs in the browser
                                      # router can only be used with viewset classes like ViewSet and ModelViewSet

router.register('category', CategoryAPI)   # regestering API classes in the router
router.register('food', FoodAPI)
router.register('table', TableAPI)
router.register('order', OrderAPI)
router.register('order-item', OrderItemAPI)
router.register('user', UserAPI)




urlpatterns = [
    
] + router.urls             # regestering router in the url patterns