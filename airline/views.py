from django.shortcuts import render
from airline.models import airline,price,order
from cab.models import Tax,wallet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
from .serializers import findSerializer,orderSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer



def addAirline(request):
    airid = request.GET.get('airlineid')
    airname = request.GET.get('name')
    Route = request.GET.get('route')
    aircomp = request.GET.get('Aircomp')
    timed = request.GET.get('timedep')
    timea = request.GET.get('timearr')

    a = airline(airlineid=airid,airlineName=airname,route=Route,airlineComp=aircomp,timedep=timed,timearr=timea)

    a.save()

    return JsonResponse({'result':1})


def addPrice(request): 

    Route = request.GET.get('route')
    prc = request.GET.get('price')
    Sseats = request.GET.get('Seats')
    Date = request.GET.get('date')
    Airlineid = request.GET.get('airline')

    a = airline.objects.get(airlineid=Airlineid)

    p = price(Airline=a,date=Date,Price = prc,seats=Sseats,route =Route)
    p.save()

    return JsonResponse({'result':1})
    

def findFlights(request):
    Route = request.GET.get('route')
    Date = request.GET.get('date')
    
    air = price.objects.filter(route=Route ,date = Date)

    print(air)
    print(air)
    c = 0
    list = []
    for a in air:
        serial = findSerializer(a)
        list.append(serial.data)
        c = c + 1

    return JsonResponse({'result':list})
    
def orderCallBack(request):
    UserNane = request.GET.get('username')
    Amount = request.GET.get('TXN_AMOUNT')
    # Route = request.GET.get('route')
    flightId= request.GET.get('flightid')
    Date = request.GET.get('date')
    Paytm = request.GET.get('paytm')

    u = User.objects.get(username=UserNane)

    complaint = random.randint(100,999) + random.randint(9999,10000) + u.pk
    
    txn = "TXN25"+str(complaint)
        
    if(Paytm == 'no'):
        transaction = Tax(user=u,amount = Amount, txnid = txn,credit = True)
        airid = airline.objects.filter(airlineid=flightId)
        wall = wallet.objects.get(user=u)
        print(airid)
        wall.amount = wall.amount - float(Amount) 
        a = order(user = u,txnid = txn,amount = Amount,Airline =airid[0],date = Date)

        wall.save()
        a.save()
        transaction.save()
    else:
        transaction = Tax(user=u,amount = Amount, txnid = txn,credit = True)
        airid = airline.objects.filter(airlineid=flightId)
        a = order(user = u,txnid = txn,amount = Amount,Airline =airid[0],date = Date)
        a.save()
        transaction.save()   


    return JsonResponse({'result':1})
    
def showorders(request):
    UserNane = request.GET.get('username')
    Cab = request.GET.get('cab')
    u = User.objects.get(username=UserNane)


    o = order.objects.filter(user=u)

    list = []

    for O in o:
        serial = orderSerializer(O)
        list.append(serial.data)
            
    return JsonResponse({'result':list})

