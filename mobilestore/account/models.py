from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custuser(AbstractUser):
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to="profile_image",null=True)
    options=(
        ("store","store"),
        ("customer","customer"),
 
    )
    usertype=models.CharField(max_length=100,choices=options,default="customer")
