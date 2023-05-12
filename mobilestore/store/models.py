from django.db import models
from account.models import Custuser

# Create your models here.
class Mobile(models.Model):
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    specs = models.TextField(null=True)
    photo = models.ImageField(upload_to='mobile_photos', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(Custuser, on_delete=models.CASCADE, related_name="m_user")
    
class Product(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.brand} {self.model}"
    
class Profile(models.Model):
    dob=models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    store_name=models.CharField( max_length=100,null=True)
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile_pictures",null=True)
    user=models.OneToOneField(Custuser,on_delete=models.CASCADE,related_name="pro_user")

class Review(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Custuser,on_delete=models.CASCADE,related_name="R_user")
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,related_name="R_post")