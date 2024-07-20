from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    clientAddress = models.CharField(max_length=200)
    contactPhone = models.CharField(max_length=20)
    contactEmail = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.apellidos}"

class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    plateNumber = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    vin = models.CharField(max_length=17)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.plateNumber})"

class Reserva(models.Model):
    idreserva = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    vehiculo = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora = models.TimeField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.vehiculo}"
