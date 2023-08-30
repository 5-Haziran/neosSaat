from django.shortcuts import render
from .models import *

# Create your views here.


def index (request,):
    
    product = Product.objects.all()
    brand = Brand.objects.all()

    
    context = {
        'product':product,
        'brand':brand
    }
    
    return render (request,'index.html',context)

def brand(request,id):
    
    brand = Product.objects.filter(brand=id)
    
    context={
        'brand':brand
    }
    
    return render(request,'brand.html',context)

def detail(request,id):
    product = Product.objects.get(id=id)
    brand = Brand.objects.all()

    if request.method =='POST':
        comment=request.POST['comment']
        commentImg = request.FILES['commentImg']
        com = Comment(commentText=comment,commentImg=commentImg)
        com.save()
        
    context ={
        'product':product,
        'brand':brand
    }
    
    return render(request,'detail.html',context)