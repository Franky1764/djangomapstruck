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
    path('accounts/', include('django.contrib.auth.urls')),
    path('cliente/', include('cliente.urls')),
    path('client-register/', views.client_register_view, name='client_register'),
    path('success', views.success_view, name='success'),
    path('reservas', views.reservas, name='reservas'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('carrito', views.carrito, name='carrito'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]