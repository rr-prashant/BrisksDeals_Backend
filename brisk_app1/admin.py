from django.contrib import admin
from . import models


#username = briskdeals pw= @brisk
#registering models
admin.site.register(models.User)
admin.site.register(models.VendorRequest)
admin.site.register(models.Cart)
admin.site.register(models.Charges)
admin.site.register(models.VendorBusinessDetails)
admin.site.register(models.Feedback)

@admin.register(models.Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display=['deal_title', 'deal_category']


admin.site.register(models.CouponActive)
admin.site.register(models.EmailNotificationModel)