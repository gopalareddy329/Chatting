from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name =models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    participents=models.ManyToManyField(User,related_name="participents",blank=True)
    def __str__(self):
        return self.name
    
    
class Messages(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField(blank=True)
    Room=models.ForeignKey(Room,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    def __str__(self):
        return self.body[0:50]