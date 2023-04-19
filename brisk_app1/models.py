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
    vendor_about = models.TextField(blank=True)
    vendor_opening_days = models.CharField(max_length=12, blank=True)
    vendor_opening_time = models.CharField(max_length=12, blank=True)
    
    
    def __str__(self):
        return self.full_name
    
class VendorRequest(models.Model):
    vendor_email = models.CharField(max_length=50, blank=True)
    vendor_BusinessName = models.CharField(max_length=50, blank=True)
    vendor_phoneNumber = models.CharField(max_length=50, blank=True)
    vendor_Location = models.CharField(max_length=50, blank=True)
    vendor_about = models.TextField(blank=True)
    vendor_opening_days = models.CharField(max_length=12, blank=True)
    vendor_opening_time = models.CharField(max_length=12, blank=True)
    
    def __str__(self):
        return self.vendor_BusinessName

# def upload_to(inst, filename):
#     return


class VendorBusinessDetails(models.Model):
    vendor_email = models.CharField(max_length=50, blank=True)
    vendor_BusinessName = models.CharField(max_length=50, blank=True)
    vendor_phoneNumber = models.CharField(max_length=50, blank=True)
    vendor_Location = models.CharField(max_length=50, blank=True)
    vendor_id = models.IntegerField(primary_key=True, default="0000")
    vendor_image = models.ImageField(null = True, blank=True)
    vendor_about = models.TextField(blank=True)
    vendor_opening_days = models.CharField(max_length=12, blank=True)
    vendor_opening_time = models.CharField(max_length=12, blank=True)
    
    def __str__(self):
        return self.vendor_BusinessName
    

    
class EmailNotificationModel(models.Model):
    notification_email = models.CharField(max_length=50,blank=True)
    notification_message = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.notification_email

class Deals(models.Model):
    user = models.ForeignKey(VendorBusinessDetails, on_delete=models.CASCADE)
    BusinessName = models.CharField(max_length=50, blank=True)
    Business_ProfileImage = models.ImageField(null= True, blank= True)
    BusinessLocation = models.CharField(max_length=50, blank=True, null=True)
    Business_Phone = models.CharField(max_length = 50, blank=True)
    deal_title = models.CharField(max_length=70)
    deal_price = models.IntegerField(blank= True, default= 0)
    deal_photo = models.ImageField(null= True, blank=True)
    deal_category = models.CharField(max_length=20)
    deal_desc = models.TextField()
    deal_condition = models.TextField(blank=True)
    deal_discount = models.IntegerField(blank= True, default= 0)
    deal_applicable_time = models.CharField(max_length=10)
    deal_applicable_day = models.CharField(max_length=10)
    deal_expiry_date = models.CharField(max_length=12)
    
    def __str__(self):
        return self.deal_title

class Cart(models.Model):
    deal_title = models.CharField(max_length=70)
    deal_price = models.IntegerField(blank= True, default= 0)
    deal_photo = models.ImageField(null= True, blank=True)
    deal_category = models.CharField(max_length=20)
    deal_desc = models.TextField()
    deal_condition = models.TextField(blank=True)
    deal_discount = models.IntegerField(blank= True, default= 0)
    deal_applicable_time = models.CharField(max_length=10)
    deal_applicable_day = models.CharField(max_length=10)
    deal_expiry_date = models.CharField(max_length=12)
    Customer_User = models.ForeignKey(User, on_delete=models.CASCADE)
    Vendor_User =  models.ForeignKey(VendorBusinessDetails, on_delete=models.CASCADE)
    VendorBusiness_Name = models.CharField(max_length = 50, blank=True)
    VendorBusiness_Location = models.CharField(max_length = 50, blank=True)
    VendorBusiness_ProfileImage = models.ImageField(null= True, blank= True)
    Vendor_Phone = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.deal_title
    

class Charges(models.Model):
    coupon_rate = models.IntegerField(blank=True, default=0)



class CouponActive(models.Model):
    deal_title = models.CharField(max_length=70, blank=True)
    deal_photo = models.ImageField(null= True, blank=True)
    deal_discount = models.IntegerField(blank= True, default= 0)
    deal_applicable_time = models.CharField(max_length=10, blank=True)
    deal_applicable_day = models.CharField(max_length=10, blank=True)
    deal_expiry_date = models.CharField(max_length=12, blank=True)
    Customer_User = models.ForeignKey(User, on_delete=models.CASCADE)
    Vendor_User = models.ForeignKey(VendorBusinessDetails, on_delete=models.CASCADE)
    VendorBusiness_Name = models.CharField(max_length = 50, blank=True)
    VendorBusiness_Location = models.CharField(max_length = 50, blank=True)
    Vendor_Phone = models.CharField(max_length = 50, blank=True)
    Total_Coupon_Price = models.IntegerField(blank= True, default= 0)
    Customer_Name = models.CharField(max_length = 50, blank=True)
    Customer_Address = models.CharField(max_length = 100, blank=True)
    Customer_Phonenumber = models.CharField(max_length = 50, blank=True)
    Customer_Email = models.CharField(max_length = 50, blank=True)
    Status = (
        ('Active', 'ACTIVE'),
        ('Used', 'USED'),
    )
    coupon_Status = models.CharField(max_length = 20, choices= Status, default= 'Active')



    def __str__(self):
        return self.Customer_Name



class Feedback(models.Model):
    Customer_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_id = models.IntegerField(blank=False, null=True)
    Customer_Name = models.CharField(max_length=70, blank=True)
    Customer_Email = models.CharField(max_length=70, blank=True)
    Feedbacks = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.Customer_Name