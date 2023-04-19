# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.views import UserDetailsView
from dj_rest_auth.registration.views import RegisterView
from django.conf import settings
from rest_framework.response import Response #SocialLoginView
from .models import Cart, Charges, CouponActive, Deals, EmailNotificationModel, User, VendorBusinessDetails, VendorRequest, Feedback
from rest_framework import generics, status
from django.core.mail import send_mail
from .serializers import CartSerializer, ChargesSerializer, CouponItemsSerializer, DealsSerializer, EmailNotificationSerializer, NewRegisterSerializer, NewUserDetailsSerializer, VendorBusinessDetailsSerializer, VendorRegisterSerializer, VendorRequestSerializer, FeedbackSerializer


# view for registered user details
class userDetails(UserDetailsView):
    queryset = User.objects.all()
    serializer_class = NewUserDetailsSerializer

# view for vendor registration process
class vendorForm(generics.ListCreateAPIView):
    queryset = VendorRequest.objects.all()
    serializer_class = VendorRequestSerializer

# View for vendor business details registration
class TodoGetCreate(generics.ListCreateAPIView):
   queryset = VendorBusinessDetails.objects.all()
   serializer_class = VendorBusinessDetailsSerializer  

# View for specificvendor business details registration
class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
   queryset = VendorBusinessDetails.objects.all()
   serializer_class = VendorBusinessDetailsSerializer

# View for customer registration
class CustomerRegistrationView(RegisterView):
    serializer_class = NewRegisterSerializer

# View for Vendor Registration
class VendorRegistrationView(RegisterView):
    serializer_class = VendorRegisterSerializer


#view for coupon charges
class ChargesView(generics.RetrieveUpdateAPIView):
   queryset = Charges.objects.all()
   serializer_class = ChargesSerializer

class ChargesViewAll(generics.ListCreateAPIView):
   queryset = Charges.objects.all()
   serializer_class = ChargesSerializer


# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter


# View for send notification
class SendEmailNotification(generics.CreateAPIView):
    queryset =EmailNotificationModel.objects.all()
    serializer_class = EmailNotificationSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #from_email = request.data.get('from_email')
        # serializer = EmailNotificationSerializer(EmailNotificationModel)
        
        
        send_mail(
            'Notification from BriskDeals.',
            serializer.data['notification_message'],
            settings.EMAIL_HOST_USER,
            [serializer.data['notification_email']],
            fail_silently=False,
        )
        
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                         status=status.HTTP_201_CREATED, headers=headers)
        

class DealsView(generics.ListCreateAPIView):
        queryset = Deals.objects.all()
        serializer_class = DealsSerializer

class DealsGCUView(generics.ListCreateAPIView):
        serializer_class = DealsSerializer  
           
        def get_queryset(self):
             vendor = self.kwargs['vendor']
             queryset = Deals.objects.filter(user = vendor)
             return queryset
         
class CartDelete(generics.RetrieveUpdateDestroyAPIView):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer

class CartListByUser(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = self.kwargs['cart']
        queryset = Cart.objects.filter(Customer_User = cart)
        return queryset
    
class CartGetCreate(generics.ListCreateAPIView):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer
   
   
   
class CouponItemsViews(generics.ListCreateAPIView):
   queryset = CouponActive.objects.all()
   serializer_class = CouponItemsSerializer

class CouponListByUser(generics.ListCreateAPIView):
    serializer_class = CouponItemsSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        queryset = CouponActive.objects.filter(Customer_User = user)
        return queryset
    
class CouponListByVendor(generics.ListCreateAPIView):
    serializer_class = CouponItemsSerializer

    def get_queryset(self):
        vendor = self.kwargs['vendor']
        queryset =CouponActive.objects.filter( Vendor_User = vendor)
        return queryset
    
class CouponUpdate(generics.RetrieveUpdateAPIView):
   queryset = CouponActive.objects.all()
   serializer_class = CouponItemsSerializer
   

class FeedbackView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer