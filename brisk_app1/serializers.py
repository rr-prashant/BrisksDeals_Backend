from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import Cart, Charges, CouponActive, Deals, EmailNotificationModel, VendorBusinessDetails, VendorRequest, Feedback


UserModel = get_user_model()

class NewUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model=UserModel
        fields=["pk","user_type","email","full_name", "location", "phonenumber", "vendor_about", "vendor_opening_days", "vendor_opening_time"]
        
class VendorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model= VendorRequest
        fields= '__all__'

class VendorBusinessDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= VendorBusinessDetails
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
    location = serializers.CharField()
    vendor_about = serializers.CharField()
    vendor_opening_days = serializers.CharField()
    vendor_opening_time = serializers.CharField()
    
    def custom_signup(self, request, user):
        user.user_type = 2
        user.full_name=request.data['full_name']
        user.phonenumber = request.data['phonenumber']
        user.location = request.data['location']
        user.vendor_about = request.data['vendor_about']
        user.vendor_opening_days = request.data['vendor_opening_days']
        user.vendor_opening_time = request.data['vendor_opening_time']
        user.save()
        
class NewLoginSerializer(LoginSerializer):
    pass


class EmailNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailNotificationModel
        fields = '__all__'
        

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = '__all__'
        
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charges
        fields = '__all__'
        

class CouponItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponActive
        fields = '__all__'      
        

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        