from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil (models.Model):
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    user= models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    userİmg = models.ImageField(("Kullanıcı fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    
class Brand (models.Model):
    title = models.CharField(("Marka"), max_length=50)
    

class Product (models.Model):
    brand= models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(("Ürün başlığı"), max_length=50)
    productİmg = models.ImageField(("Ürün fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)
    productColor = models.CharField(("Renk kodunu gir"), max_length=50)
    productDesct = models.TextField(("Ürün açıklaması"))
    productSıze = models.CharField(("Ürünün boyutu"), max_length=50)
    productPrice = models.PositiveIntegerField(("Ürünün fiyatı"),default=0)
    
    productGender = models.CharField(("Ürünün Cinsiyeti"), max_length=50, choices=(('kadın',True),('erkek',False)))
    
    productStock = models.PositiveIntegerField(("Ürün stok"))
    liked = models.ManyToManyField(User,related_name=("liked_product"),blank=True)
    
class Comment (models.Model):
    comment= models.ForeignKey(Product, verbose_name=("Ürün adı"), on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    commentText = models.TextField(("Yorum"))
    commentImg = models.ImageField(("Yorum Görseli"), upload_to=None, height_field=None, width_field=None, max_length=None)
    commentDate = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    