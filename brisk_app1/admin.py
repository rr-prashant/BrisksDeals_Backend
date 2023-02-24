from django.contrib import admin
from . import models


#username = briskdeals pw= @brisk
#registering models
admin.site.register(models.User)
admin.site.register(models.VendorRequest)