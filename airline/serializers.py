from rest_framework import serializers
from django.contrib.auth.models import User
from airline.models import price,airline
from cab.models import cabDetail,CabOrder

class airlineSerializer(serializers.Serializer):
    airlineid = serializers.CharField()
    route = serializers.CharField()
    airlineComp = serializers.CharField()
    timedep = serializers.CharField()
    timearr = serializers.CharField()

class findSerializer(serializers.Serializer):
    Airline = airlineSerializer()
    Price = serializers.FloatField()
    seats= serializers.IntegerField()
    route = serializers.CharField()
    date = serializers.DateField()

class orderSerializer(serializers.Serializer):
    txnid = serializers.CharField()
    amount = serializers.FloatField()
    Airline = airlineSerializer()
    date = serializers.CharField()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
class CabDetailSerializer(serializers.Serializer):
    numb = serializers.CharField()
    CabModel = serializers.CharField()

class CabSerializer(serializers.Serializer):
    user = UserSerializer()
    orderid = orderSerializer()
    cab = CabDetailSerializer()
    longitude = serializers.CharField()
    latitude = serializers.CharField()
    pickuplat = serializers.CharField()
    pickuplong = serializers.CharField()
    amount = serializers.CharField()