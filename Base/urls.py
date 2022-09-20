from django.urls import path,include
from . import views 

urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginuser,name="login"),
    path('logoutuser/',views.logoutuser,name="logout"),
    
]