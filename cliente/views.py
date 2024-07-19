from django.shortcuts import render, redirect
from .forms import ClientForm, VehicleForm, ReservaForm
from django.contrib import messages
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    context = {}
    return render(request, 'cliente/index.html', context)

def contacto(request):
    context = {}
    return render(request, 'cliente/contacto.html', context)

def nosotros(request):
    context = {}
    return render(request, 'cliente/nosotros.html', context)

def servicios(request):
    context = {}
    return render(request, 'cliente/servicios.html', context)

def client_register_view(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        vehicle_form = VehicleForm(request.POST)
        if client_form.is_valid() and vehicle_form.is_valid():
            client_form.save()
            vehicle_form.save()
            messages.success(request, '¡Registro completado exitosamente!')
            return redirect('client_register')
    else:
        client_form = ClientForm()
        vehicle_form = VehicleForm()
    return render(request, 'cliente/client_register.html', {'client_form': client_form, 'vehicle_form': vehicle_form})

def success_view(request):
    return render(request, 'cliente/success.html')

def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Procesar la reserva y guardar en la base de datos si es necesario
            return redirect('success')
    else:
        form = ReservaForm()
    return render(request, 'cliente/reservas.html', {'form': form})

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'clp',
                            'product_data': {
                                'name': 'Revisión Técnica',
                            },
                            'unit_amount': 500000,  # Precio en centavos de CLP (5000 CLP)
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='https://your-domain.com/success/',
                cancel_url='https://your-domain.com/cancel/',
            )
            return JsonResponse({
                'id': checkout_session.id
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

def carrito(request):
    context = {}
    return render(request, 'cliente/carrito.html', context)

def success_view(request):
    return render(request, 'cliente/success.html')