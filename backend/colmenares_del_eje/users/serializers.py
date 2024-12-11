from rest_framework import serializers
from users.models import User, Login

class InputUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    assignment_date = serializers.DateField()
    birth_date = serializers.DateField()
    state = serializers.CharField()
    role = serializers.CharField()
    

class OutputUserSerializer(InputUserSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")
    
class LoginInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)
    dateLogin = serializers.DateTimeField(source="date_login")
    idSignup = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
class LoginOutputSerializer(serializers.Serializer):
    username = serializers.CharField()
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")