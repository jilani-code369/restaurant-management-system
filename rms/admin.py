from django.contrib import admin
from .models import *

# Register your models here.


# Customizing admin panel

## Customizing Category table in admin panel: 
@admin.register(Category)                 # Using decorator to register table in admin panel 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


## Customizing 'Food' table: 
@admin.register(Food)     
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category']
    list_display_links = ['id', 'name']
    list_editable = ['price']
    list_filter = ['category']
    search_fields = ['name', 'category__name']      # In 'category__name',  double underscore '__' is used to lookup in the foreign key. 
    list_per_page = 10
    

## Customizing 'Table' table
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'capacity', 'available']
    list_display_links = ['id', 'table_number']
    list_editable = ['available']
    search_fields = ['table_number', 'capacity']
    list_filter = ['available', 'capacity']


## Customizing 'Order' table
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'food', 'table', 'total_price', 'status', 'payment_status']
    list_display_links = ['id', 'user', 'food']
    list_editable = ['status', 'payment_status']
    list_filter = ['status', 'payment_status']
    search_fields = ['user__username', 'food__name', 'table__table_number']
    list_per_page = 10



## Customizing 'OrderItem' table:
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'food']
    list_display_links = ['id', 'order','food']
    


## Registering tables in  admin panel 
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Food, FoodAdmin)
# admin.site.register(Table, TableAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
