from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('servicios', views.servicios, name='servicios'),
]