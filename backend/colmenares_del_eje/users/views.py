from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import InputUserSerializer, OutputUserSerializer, LoginInputSerializer, LoginOutputSerializer
from users.models import User, Login

class sign_up_view(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        serializer = InputUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if User.objects.filter(username=serializer.validated_data["username"]).exists():
            return Response("El Usuario ya está registrado", status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=serializer.validated_data["email"]).exists():
            return Response("El email ya está registrado", status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(**serializer.validated_data)
        
        refresh = RefreshToken.for_user(user)
        
        serializer = OutputUserSerializer({
            "username": user.username,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "assignment_date": user.assignment_date,
            "birth_date": user.birth_date,
            "state": user.state,
            "role": user.role,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class login_view(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = User.objects.get(username=serializer.validated_data['username'])
        except User.DoesNotExist:
            return Response("Usuario o Contraseña es incorrecta", status=status.HTTP_400_BAD_REQUEST)
        
        is_password_correct = user.check_password(serializer.validated_data['password'])
        if is_password_correct is False:
            return Response("Usuario o Contraseña es incorrecta", status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)


        serializer = LoginOutputSerializer({
            "username": user.username,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)