from django.db import models
from django.contrib.auth.models import User
from appMy.models import *

# Create your models here.


class Profil (models.Model):
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    user= models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True,blank=True)
    userİmg = models.ImageField(("Kullanıcı fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self) -> str:
        return self.user