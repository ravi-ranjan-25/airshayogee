from django.shortcuts import render
from cab.models import userMob,Tax,wallet,CabOrder,cabDetail
from airline.models import airline,price,order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
from .serializers import TaxSerializer
from airline.serializers import CabSerializer
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
        wall = wallet.objects.get(user = user1)
        return JsonResponse({'result':1,'username':user1.username,'email':user1.email,'firstname':user1.first_name,
                                'lastname':user1.last_name,'mobile':house.mobile,'balance':wall.amount,'admin':house.admin,'cab':house.cab})
    
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

        transaction.credit = False
        wall1.save()
        transaction.save()
        return JsonResponse({'result':1})

class TaxListView(ListAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
   
def orderCab(request):
    Txn = request.GET.get('txnid')   
    username1 = request.GET.get('username')
    longi = request.GET.get('longitude')
    lati = request.GET.get('latitude')
    Pickupl = request.GET.get('pickuplong')     
    Pickupla = request.GET.get('pickuplat')

    user1 = User.objects.get(username = username1)
    
    o = order.objects.get(txnid = Txn)

    cr = CabOrder(user = user1,orderid=o,longitude=longi,latitude=lati,pickuplong=Pickupl,pickuplat=Pickupla)    
    
    cr.save()
    return JsonResponse({'result':1})


def showUserCab(request):    
    username1 = request.GET.get('username')
    user1 = User.objects.get(username = username1)

        
    c = CabOrder.objects.filter(user = user1)

    
    list = []
    
    for C in c:
        serial = CabSerializer(C)

        list.append(serial.data)

    return JsonResponse({'result':list})

def showDriver(request):    
    
        
    c = CabOrder.objects.filter(cab = None)

    
    list = []
    
    for C in c:
        serial = CabSerializer(C)

        list.append(serial.data)

    return JsonResponse({'result':list})

def assigncab(request):
    username1 = request.GET.get('username')
    Txn = request.GET.get('txnid')   

    user1 = User.objects.get(username = username1)
    cabD = cabDetail.objects.get(user = user1)
    o = order.objects.get(txnid = Txn)    
    c = CabOrder.objects.get(orderid = o)


    c.cab = cabD
    c.save()

    return JsonResponse({'result':1})
