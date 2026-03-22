from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Change admin.site.register to admin.site.urls
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
]
