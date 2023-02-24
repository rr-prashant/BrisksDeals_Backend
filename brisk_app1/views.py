from django.shortcuts import render
from dj_rest_auth.views import UserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .models import User, VendorRequest
from rest_framework import generics
from .serializers import NewRegisterSerializer, NewUserDetailsSerializer, VendorRegisterSerializer, VendorRequestSerializer

class userDetails(UserDetailsView):
    queryset = User.objects.all()
    serializer_class = NewUserDetailsSerializer
    
class vendorForm(generics.ListCreateAPIView):
    queryset = VendorRequest.objects.all()
    serializer_class = VendorRequestSerializer

class CustomerRegistrationView(RegisterView):
    serializer_class = NewRegisterSerializer

class VendorRegistrationView(RegisterView):
    serializer_class = VendorRegisterSerializer