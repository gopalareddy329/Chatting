from django.shortcuts import render,redirect
from .forms import Userform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'Base/home.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,'Base/login.html')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        return redirect('home')
    return render(request,'Base/login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def signup(request):
    form=Userform()
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            user.save()
            return redirect('home')

            
            
    context={'forms':form}
    return render(request,'Base/signup.html',context)