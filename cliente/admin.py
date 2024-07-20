from django.contrib import admin
from .models import Client, Vehicle, Reserva
# Register your models here.



admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(Reserva)