from rest_framework import serializers
from django.contrib.auth.models import User
from airline.models import price,airline

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
        