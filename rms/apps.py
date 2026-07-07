from django.apps import AppConfig


class RmsConfig(AppConfig):
    name = 'rms'
    
    def ready(self):
        import rms.signals




# How ready() function works: 

# Django starts
#       ↓
# Django loads installed apps
#        ↓
# Django calls ready()
#       ↓
# ready() imports rms.signals
#       ↓
# signals get registered