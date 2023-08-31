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
    brands = Brand.objects.all()
    
    context={
        'brand':brand,
        'brands':brands
    }
    
    return render(request,'brand.html',context)

def detail(request,id):
    product = Product.objects.get(id=id)
    brand = Brand.objects.all()
    comments = Comment.objects.filter(product_id=product)

    if request.method =='POST':
        comment=request.POST['comment']
        commentImg = request.FILES.get('commentImg')
        
        if commentImg:
            com = Comment(commentText=comment,commentImg=commentImg,product_id=id)
            com.save()
            
        else:
            com = Comment(commentText=comment,product_id=id)
            com.save()
       
    context ={
        'product':product,
        'brand':brand,
        'comments':comments,
    }
    
    return render(request,'detail.html',context)