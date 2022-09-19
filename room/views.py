from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'room/room.html',{'rooms':rooms})

@login_required(login_url='login')
def chat(request,slug):
    room=Room.objects.get(slug=slug)
    
    return render(request,'room/chat.html',{'content':room})