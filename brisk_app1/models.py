from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    type = ((1, 'Customer'),
            (2, 'Vendor'))
    user_type = models.IntegerField(choices=type, default= 1)
    username = models.CharField(max_length=55, unique=False)
    full_name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phonenumber = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.full_name
    
class VendorRequest(models.Model):
    email = models.CharField(max_length=50, blank=True)
    BusinessName = models.CharField(max_length=50, blank=True)
    phoneNumber = models.CharField(max_length=50, blank=True)
    Location = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.BusinessName