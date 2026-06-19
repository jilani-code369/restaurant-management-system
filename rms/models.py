from django.db import models 
from django.contrib.auth import get_user_model    # import this to use the default User in django

# Create your models here.


#1. User table: 
User = get_user_model()     # it fetches the active user model from the project (can be either default or custom).


#2. Category table: 
class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):             # this is a dunder function. It displays object as a string in admin panel. 
        return self.name
        

#3. Food table: 
class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def __str__(self):       
        return self.name


#4. Table table: 
class Table(models.Model):
    table_number = models.CharField(max_length=15)  # 'CharField' is used bec. table number can be 'A','B','C' also.
    capacity = models.IntegerField()
    available = models.BooleanField(default = True)
    
    def __str__(self):             
        return self.table_number


#5. Order table: 
class Order(models.Model):
    STATUS_CHOICES= [               # enum for status
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("delivered", "Delivered")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null = True)
    total_price = models.FloatField(null = True)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default = 'pending')
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"User: {self.user} - {self.table}"
    

#6. OrderItem junction table: 

## Junction table is used here to create many-to-many relation between order and food. 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)

