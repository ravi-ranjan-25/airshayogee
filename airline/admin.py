from django.contrib import admin
from airline.models import airline,price,order
# Register your models here.
admin.site.register(price)
admin.site.register(order)
admin.site.register(airline)

