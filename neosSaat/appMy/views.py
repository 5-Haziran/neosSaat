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

def detail(request,id):
    product = Product.objects.get(id=id)

    context ={
        'product':product
    }
    
    return render(request,'detail.html',context)