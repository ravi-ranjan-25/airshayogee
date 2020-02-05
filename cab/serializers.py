from rest_framework import serializers
from django.contrib.auth.models import User
from cab.models import Tax

class TaxSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('Complain')
    
    class Meta:
        model = Tax
        fields = '__all__'

    def Complain(self,wall): 
         user1 = wall.user.username
         return user1

class TranSerializer(serializers.Serializer):
    txnid = serializers.CharField()
    amount = serializers.FloatField()
    credit = serializers.BooleanField()
    time = serializers.DateTimeField()