from django.shortcuts import render,redirect
from appMy.templates import *
from .models import * 
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
        else:
            context = {
                'information':'Girmiş olduğunuz bilgiler hatalıdır. Tekrar deneyiniz.'
            }
        
            return render(request,'part/login.html',context)
    
    return render(request,'part/login.html')

def logoutt(request):
    
    logout(request)
    
    return redirect('anasayfa')

def profil(request):
    
    profil = Profil.objects.get(user=request.user)
    
    if request.user.is_authenticated:       
        try:
            user_profil = Profil.objects.get(user=request.user)
                
        except Profil.DoesNotExist:
            user_profil = Profil(user=request.user)
            user_profil.save()
                
    if request.method =="POST" and 'profil-img-btn' in request.POST:
        filee = request.FILES.get('profil-img')
        
        if filee:
            user_profil.userİmg =filee
            user_profil.save()
            
            
    if request.method =="POST" and 'person-btn' in request.POST:
        
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        
        user.save()                
    context ={
        'profil':profil
    }
    return render(request,'profil.html',context)