from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class userMob(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.CharField(unique = True,max_length=256)
    admin = models.BooleanField(default=False)
    time = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.mobile

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