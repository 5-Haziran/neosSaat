from django.shortcuts import render,redirect
from appMy.templates import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def register(request):
    
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname =request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=firstname).exists():
                context = {
                    'information':'Böyle bir kullanıcı mevcut, farklı bir kullanıcı adıyla deneyin'
                }
                return render(request,'part/register.html',context)
            
            if User.objects.filter(email=email).exists():
                context = {
                    'information':'Sisteme kaydetmek istediğiniz e-posta adresi kullanılmaktadır. Farklı bir e-posta adresiyle kayıt olmayı deneyin.'
                }
                
                return render (request,'part/register.html',context)
            
            else: 
                user = User.objects.create_user(username=firstname,last_name=lastname,first_name=firstname,email=email,password=password)
                user.save()
                
                context = {
                    'information':'Kayıt işleminiz gerçekleştirilmiştir.'
                }
                
                return render(request,'part/register.html',context)
        else:
            context = {
                'information':'Parolanız girdiğiniz parolayla uyuşmuyor, kontrol ederek tekrar deneyin.'
            }
            
            return render(request,'part/register.html',context)
    
    return render(request,'part/register.html')


def loginn(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            
            return redirect('anasayfa')
        
    
    return render(request,'part/login.html')

def logoutt(request):
    
    logout(request)
    
    return redirect('anasayfa')