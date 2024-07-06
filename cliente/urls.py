from django.urls import path
from .views import index
from .views import contacto
from .views import nosotros
from .views import servicios

urlpatterns = [
    path('', index, name='index')
]

urlpatterns = [
    path('', contacto, name='contacto')
]

urlpatterns = [
    path('', nosotros, name='nosotros')
]

urlpatterns = [
    path('', servicios, name='servicios')
    
]