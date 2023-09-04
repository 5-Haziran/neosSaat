from django.shortcuts import render
from .models import *
from user.views import *
from django.db.models import Q


# Create your views here.


def index (request,):
    
    product = Product.objects.all()
    brand = Brand.objects.all()
    
    query = request.GET.get('q')
    if query:
        product = product.filter(
            Q(title__icontains=query)|
            Q(productDesct__icontains=query)|
            Q(productGender__icontains=query)|
            Q(brand__title__icontains=query)
        ).distinct

    
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

def urunekle(request,id):
    
    product = Product.objects.get(id=id)
    user = request.user
    sepet = Sepet.objects.create(user=user,product=product,adet=1, allprice = product.productPrice)
    
    sepet.save()
    return redirect('sepet')
    
def shopping(request):
    sepet = Sepet.objects.filter(user=request.user)
    toplam = 0
    
    for item in sepet:
        toplam+=item.product.productPrice * item.adet
    
    context = {
        'sepet':sepet,
        'toplam':toplam
    }
    return render(request,'shopping.html',context)

def ürünSil (request,id):
    
    if request.method =='POST':
        sepet_item = Sepet.objects.get(id=id)
        sepet_item.delete()
        
        return redirect('sepet')
    
def ürünGüncelle(request,id):
    
    if request.method == 'POST':
        sepet_item =Sepet.objects.get(id=id)
        quantity = int(request.POST.get('quantity',1))
        sepet_item.adet =quantity
        sepet_item.allprice = sepet_item.product.productPrice * quantity
        sepet_item.save()
        
        return redirect('sepet')