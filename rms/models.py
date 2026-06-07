from django.db import models 
from django.contrib.auth import get_user_model     # Import this to use the default User in django

# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length = 20)
    
class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank = True)

class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    available = models.BooleanField()


class Order(models.Model):
    STATUS_CHOICES= [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("delivered", "Delivered")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null = True, blank = True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null = True, blank = True)
    total_price = models.FloatField()
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default = 'pending')
    payment_status = models.BooleanField()
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)