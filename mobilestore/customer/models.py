from django.db import models
from account.models import Custuser
from store.models import Mobile
from django.conf import settings


class Cart(models.Model):
    user = models.OneToOneField(Custuser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE) # use the string 'Product' here
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
class MyOrders(models.Model):
    user = models.ForeignKey(Custuser, on_delete=models.CASCADE) 
    address = models.CharField(max_length=1000) 
    sub_total = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

class OrderItems(models.Model):
    order = models.ForeignKey(MyOrders, on_delete=models.CASCADE)
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    review = models.TextField()

      

class Product(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.brand + ' ' + self.model
