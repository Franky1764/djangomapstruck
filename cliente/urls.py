from django.contrib import admin
from django.urls import path
from . import views
from cliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('servicios', views.servicios, name='servicios'),
    path('admin/', admin.site.urls),
    path('client-register/', views.client_register_view, name='client_register'),
    path('success/', views.success_view, name='success'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
]