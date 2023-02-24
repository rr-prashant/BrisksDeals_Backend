

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useraccounts/', include('brisk_app1.urls')),

    
    
    # path('api-auth/', include('rest_framework.urls')),
    # path('account/',include('allauth.urls'))
]
