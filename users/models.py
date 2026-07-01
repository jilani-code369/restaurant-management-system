from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ROLES_CHOICES = [
        ("customer", "Customer"),
        ("waiter", "Waiter"),
        ("admin", "Admin")  
    ]
    role = models.CharField(max_length=15, choices = ROLES_CHOICES)
    phone = models.CharField(max_length=15, unique = True, null = True)
    
    #USERNAME_FIELD = 'phone'       # 'USERNAME_FIELD' : sets login field (eg: 'phone' or 'email')
    #USERNAME_FIELD = 'email' 
    
    def __str__(self):
        return self.username
    
    