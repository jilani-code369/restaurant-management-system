from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


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
