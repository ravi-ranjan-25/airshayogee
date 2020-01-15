from django.shortcuts import render
from cab.models import userMob
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse

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

        # Return 1
        return JsonResponse({'result':1,'message':'success'})

def login(request):
    userName = request.GET.get('username')
    Password = request.GET.get('password')
    

    user1 = authenticate(username=userName, password=Password)
    house = userMob.objects.get(user = user1)

    
    return JsonResponse({'result':1,'username':user1.username,'email':user1.email,'firstname':user1.first_name,
                                'lastname':user1.last_name,'mobile':house.mobile})
    