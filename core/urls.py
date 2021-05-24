from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('massadmin.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
]
