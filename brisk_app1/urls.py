from dj_rest_auth.registration.views import VerifyEmailView
from django.contrib import admin
from django.urls import path,include
from brisk_app1.views import CustomerRegistrationView, VendorRegistrationView, vendorForm



urlpatterns = [
    path('auth/',include('dj_rest_auth.urls')),
    path('auth/registration/',include('dj_rest_auth.registration.urls')),
    path('auth/confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('registration/customer/', CustomerRegistrationView.as_view(), name = 'Customer Register' ),
    path('registration/vendor/', VendorRegistrationView.as_view(), name = 'Vendor Register' ),
    path('unverifiedVendor/',vendorForm.as_view(), name='Unverified Vendors')
]
