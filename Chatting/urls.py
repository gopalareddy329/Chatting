
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('rooms/',include('room.urls')),
    path('admin/', admin.site.urls),
    path('',include('Base.urls')),
    
]
