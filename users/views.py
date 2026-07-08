from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.http import HttpResponse


# Create your views here.

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            raise serializers.ValidationError({"error":"Both fields are required."})    #raising error if any one field is left empty

        user = authenticate(username = username, password = password)       # it checks if the user exists or not. authenticate used to deal with the password authenticating
        if user:
            token, created = Token.objects.get_or_create(user = user)
            return Response({
                "message":"Login successful",
                "user id" : user.id,
                "username" : user.username,
                "token" : token.key
            })
        
        return Response({"error":"Invalid useranme or password."})




# Sessions: 

# set session:

def set_session(request):
    request.session['username'] = "Jilani"
    request.session['course'] = "Django"
    return HttpResponse("Session set successfully.")

# get session: 

def get_session(request):
    ussername = request.session.get('username')
    course = request.session.get('course')
    return HttpResponse(f"Username: {ussername}, Password: {course}")
    

# delete session: 

def delete_session(request):
    # del request.session['username']
    # del request.session['course']
    request.session.flush()
    return HttpResponse("Session deleted successfullly.")
    
    
    
    
    
    

# what 'request' parameter contains: ---------------------------------------- 
  
# request.method        # GET, POST, PUT, DELETE, etc.
# request.GET           # query parameters from URL
# request.POST          # form data
# request.data          # API body data, in DRF
# request.user          # logged-in user
# request.COOKIES       # cookies sent by browser
# request.session       # session data for this browser/user
# request.headers       # request headers



# how session works: ------------------------------------------------------

# user send request in the browser to set set_session
#               ↓
# djnago stores the session in the session table in the db with key and data and send the session id to the browser
#               ↓
# browser stores it as a cookie in the browser
#               ↓
# user request to get the set_session
#               ↓
# browser send the sessionid to the db
#               ↓
# db search for the key in the session table 
#               ↓
# if found return the session data
#               ↓
# same process for deleting the session.

