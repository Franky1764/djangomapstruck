from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'apellidos', 'clientAddress', 'contactPhone', 'contactEmail']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year', 'plateNumber', 'color', 'vin', 'owner']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'apellido', 'vehiculo', 'fecha', 'hora']