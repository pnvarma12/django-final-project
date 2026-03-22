from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.register),
    path('onlinecourse/', include('onlinecourse.urls')),
]
