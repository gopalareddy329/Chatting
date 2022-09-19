from django.urls import path
from . import views 

urlpatterns=[
    path('',views.rooms,name="rooms"),
    path('chat/<slug:slug>/',views.chat,name="chat"),
]