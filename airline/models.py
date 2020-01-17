from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class airline(models.Model):
    
    airlineid = models.CharField(unique = False,max_length=256)
    
    airlineName = models.CharField(unique = False,max_length=256)
    route = models.CharField(unique = False,max_length=256)
    airlineComp = models.CharField(unique = False,max_length=256)
    timedep = models.CharField(unique = False,max_length=256)
    timearr = models.CharField(unique = False,max_length=256)
    

    def __str__(self):
        return self.airlineName

class price(models.Model):
    
    Airline = models.ForeignKey(airline,on_delete = models.CASCADE)
    date = models.CharField(unique = False,max_length=256)
    Price = models.FloatField(max_length=10)
    seats= models.IntegerField(max_length=10)
    route = models.CharField(unique = False,max_length=256)

    def __str__(self):
        return self.date

class order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    txnid = models.CharField(max_length = 256)
    amount = models.FloatField(max_length=10)
    Airline = models.ForeignKey(airline,on_delete = models.CASCADE)
    date = models.CharField(unique = False,max_length=256)
    droplocation = models.CharField(unique=False,default='no',max_length=256)

    def __str__(self):
        return self.txnid
