from django_filters import FilterSet
from .models import *

class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'category' : ['exact'],    #OR,'category__name' : ['icontains'],
            'price' : ['gt', 'lt']
        }