from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    apellidos = forms.CharField(label='Apellidos', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}))
    clientAddress = forms.CharField(label='Dirección', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su dirección'}))
    contactPhone = forms.CharField(label='Teléfono de contacto', max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Teléfono de contacto'}))
    contactEmail = forms.EmailField(label='Email de contacto', required=True, widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@email.com'}))

class VehicleForm(forms.Form):
    brand = forms.CharField(label='Marca', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese la marca del vehículo'}))
    model = forms.CharField(label='Modelo', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el modelo del vehículo'}))
    year = forms.IntegerField(label='Año', required=True, widget=forms.NumberInput(attrs={'placeholder': 'Ingrese el año del vehículo'}))
    plateNumber = forms.CharField(label='Número de Placa', max_length=10, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el número de placa'}))
    color = forms.CharField(label='Color', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el color del vehículo'}))
    vin = forms.CharField(label='Número de Identificación del Vehículo (VIN)', max_length=17, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el VIN del vehículo'}))
    ownerName = forms.CharField(label='Nombre del Propietario', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del propietario'}))

class ReservaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    vehiculo = forms.CharField(max_length=100)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))