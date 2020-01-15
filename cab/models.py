from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class userMob(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.CharField(unique = True,max_length=256)
    time = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.mobile
        
