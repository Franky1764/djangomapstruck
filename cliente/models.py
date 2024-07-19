from django.db import models

# Create your models here.
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