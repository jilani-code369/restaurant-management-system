from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UA):
    # Customize the admin panel of users
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']      # don't include 'password' in the list_display, it cause security issue and also looks messy
    list_display_links = ['id', 'username']
    list_editable = ['is_staff', 'is_active', 'is_superuser']
    
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'role']
    list_per_page = 10
    
    
    # Customize the layout of the user profile editing page 
    fieldsets = (
        ( "Credential info", { "fields" : ("username", "password")}    ),
        ( "Personal info", { "fields" : ("first_name", "last_name", "email", "role", "phone") }   ),
        ( "Permissions" , { "fields" : ( "is_staff", "is_active", "is_superuser" ) }   ),
        ( "Groups" , {"fields" : ("groups", "user_permissions") }   ),
        ( "Dates" , { "fields" : ("date_joined", "last_login") } )
    )
    
    

    