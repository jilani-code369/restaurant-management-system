from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import *

@receiver(post_save, sender = Order)    # it register the model(Order) with the signal(post_save)
def notify(sender, instance, created, **kwargs):
    print(f"Order {instance.id} has been successfully created.")
    
    send_mail(
        "Order created",
        f"Your Order {instance.id} has been successfully created.",
        settings.EMAIL_HOST_USER,
        ["dearjinni44@gmail.com", "maxhn6@gmail.com"]
    )
    
# post_save.connect(notify,sender = Order)





# How signal works:--------------------------------------------------------- 

# First, Django registers/connects your function with the signal (post_save)
#
# by using: 
# post_save.connect(send_order_email, sender=Order)
#
# or by using:
# @receiver(post_save, sender=Order)
#
# Then later:
# 
# Order is saved
#       ↓
# Django sends post_save signal
#       ↓
# Django checks if any function is connected to post_save for Order
#       ↓
# If found: runs that function
#       ↓
# If not found: nothing extra happens, normal save already happened