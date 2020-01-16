from django.shortcuts import render
from cab.models import userMob,Tax,wallet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
from .serializers import TaxSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


# Create your views here.
def signup(request):
    userName = request.GET.get('username')
    eMail = request.GET.get('email')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    Password = request.GET.get('password')
    Mobile = request.GET.get('mobile')
    
    
    check = User.objects.filter(username = userName)
    checkEmail = User.objects.filter(email = eMail)
    checkHouse = userMob.objects.filter(mobile=Mobile)
   
    if len(check) > 0:
        
            return JsonResponse({'result':0,'message':'Username already exist'})
    
    elif len(checkEmail) > 0:

            return JsonResponse({'result':0,'message':'Email address already exist'})


    elif len(checkHouse) > 0:
             return JsonResponse({'result':0,'message':'Mobile already registered'})
    else:
        
        user1 = User.objects.create_user(username = userName, email=eMail, password=Password, first_name = firstname , last_name = lastname)
        house_add = userMob(mobile = Mobile)
        house_add.user = user1
        house_add.save()

        Wallet = wallet()
        Wallet.user = user1
        Wallet.save()          

        # Return 1
        return JsonResponse({'result':1,'message':'success'})

def login(request):
    userName = request.GET.get('username')
    Password = request.GET.get('password')
    

    user1 = authenticate(username=userName, password=Password)
    
    if user1 is not None:
        house = userMob.objects.get(user = user1)
    
        return JsonResponse({'result':1,'username':user1.username,'email':user1.email,'firstname':user1.first_name,
                                'lastname':user1.last_name,'mobile':house.mobile})
    
    else:
        return JsonResponse({'result':0,'message':'Incorrect username or password'})

def paytmCall(request):
        username1 = request.GET.get('username')
        am = request.GET.get('TXN_AMOUNT')

        user1 = User.objects.get(username = username1)
        
        complaint = random.randint(100,999) + random.randint(9999,10000) + user1.pk
    
        txn = "TXN25"+str(complaint)
        wall1 = wallet.objects.get(user=user1)
        
        
        transaction = Tax(amount = am, txnid = txn)
        wall1.amount = wall1.amount + float(am)
        transaction.user = user1

        transaction.credit = True
        wall1.save()
        transaction.save()
        return JsonResponse({'result':1})

class TaxListView(ListAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
   