from email import message
from django.shortcuts import render
from .models import Room,Messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'room/room.html',{'rooms':rooms})

@login_required(login_url='login')
def chat(request,slug):
    room=Room.objects.get(slug=slug)
    messages=room.messages_set.all()
    participents=room.participents.all()
    if request.method=="POST":
        content=request.POST.get('message')
        message=Messages.objects.create(
            host=request.user,
            body=request.POST.get('message'),
            Room=room
        )
        room.participents.add(request.user)
    return render(request,'room/chat.html',{'content':room,'messages':messages,'participents':participents})