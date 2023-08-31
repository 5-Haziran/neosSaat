from django.shortcuts import render
from appMy.templates import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout


# Create your views here.

def loginn(request):
    
    return render(request,'part/login.html')

def register(request):
    
    
    
    return render(request,'part/register.html')