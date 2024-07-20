from django.contrib import admin
from django.urls import path, include
from cliente import views as cliente_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cliente_views.index, name='index'),
    path('nosotros', cliente_views.nosotros, name='nosotros'),
    path('contacto', cliente_views.contacto, name='contacto'),
    path('servicios', cliente_views.servicios, name='servicios'),
    path('client-register/', cliente_views.client_register_view, name='client_register'),
    path('success', cliente_views.success_view, name='success'),
    path('reservas', cliente_views.reservas, name='reservas'),
    path('create-checkout-session/', cliente_views.create_checkout_session, name='create_checkout_session'),
    path('carrito', cliente_views.carrito, name='carrito'),
    path('signup/', cliente_views.signup, name='signup'),
    path('clients/', cliente_views.client_list, name='client_list'),
    path('clients/new/', cliente_views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', cliente_views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', cliente_views.client_delete, name='client_delete'),
    path('reservas/<int:pk>/edit/', cliente_views.modificareserva, name='modificareserva'),
    path('accounts/', include('django.contrib.auth.urls')),
]
