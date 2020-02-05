from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from airline.models import order

# Create your models here.

class userMob(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.CharField(unique = True,max_length=256)
    admin = models.BooleanField(default=False)
    cab = models.BooleanField(default=False)
    time = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.mobile

class cabDetail(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    numb = models.CharField(max_length=256)
    CabModel = models.CharField(max_length=256)
    time = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.numb


class wallet(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    amount = models.FloatField(max_length=10,default = 0.00)


class Tax(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    txnid = models.CharField(max_length = 256)
    amount = models.FloatField(max_length=10)
    credit = models.BooleanField(default=False)
    time = models.DateTimeField(default = timezone.now())


    def __str__(self):
        return self.txnid

class CabOrder(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    orderid = models.ForeignKey(order,on_delete = models.CASCADE)
    longitude = models.CharField(max_length=256,default = '0.00')
    latitude = models.CharField(max_length=256,default = '0.00')
    pickuplong = models.CharField(max_length=256,default = '0.00')
    pickuplat = models.CharField(max_length=256,default = '0.00')
    cab = models.ForeignKey(cabDetail,on_delete = models.CASCADE,blank=True,null=True)
    amount = models.FloatField(max_length=10,default=0)
    time = models.DateTimeField(default = timezone.now())
    

    def __str__(self):
        return self.longitude
