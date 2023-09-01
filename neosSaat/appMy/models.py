from django.db import models
from django.contrib.auth.models import User
from user.models import *

# Create your models here.
    
class Brand (models.Model):
    title = models.CharField(("Marka"), max_length=50)
    
    def __str__(self) -> str:
        return self.title
    

class Product (models.Model):
    brand= models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(("Ürün başlığı"), max_length=50)
    productİmg = models.ImageField(("Ürün fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)
    productColor = models.CharField(("Renk gir"), max_length=50)
    productDesct = models.TextField(("Ürün açıklaması"))
    productPrice = models.PositiveIntegerField(("Ürünün fiyatı"),default=0) 
    productGender = models.CharField(("Ürünün Cinsiyeti"), max_length=50, choices=(('Kadın','Kadın'),('Erkek','Erkek')))
    productStock = models.PositiveIntegerField(("Ürün stok"))
    liked = models.ManyToManyField(User,related_name=("liked_product"),blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Comment (models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    commentText = models.TextField(("Yorum"))
    commentImg = models.ImageField(("Yorum Görseli"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    commentDate = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    

    