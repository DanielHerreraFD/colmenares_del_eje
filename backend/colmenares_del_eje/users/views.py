from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class sign_up_view(APIView):
    pass

class login_view(APIView):
    pass

class logout_view(APIView):
    pass