from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import VendorRequest


UserModel = get_user_model()

class NewUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model=UserModel
        fields=["pk","user_type","email","full_name", "location", "phonenumber"]
        
class VendorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model= VendorRequest
        fields= '__all__'


class NewRegisterSerializer(RegisterSerializer):
    full_name =serializers.CharField()
    def custom_signup(self, request, user):
        user.user_type = 1
        user.full_name=request.data['full_name']
        user.save()
        
class VendorRegisterSerializer(RegisterSerializer):
    full_name =serializers.CharField()
    phonenumber = serializers.CharField()
    def custom_signup(self, request, user):
        user.user_type = 2
        user.full_name=request.data['full_name']
        user.phonenumber = request.data['phonenumber']
        user.save()
        
class NewLoginSerializer(LoginSerializer):
    pass