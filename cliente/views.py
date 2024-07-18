from django.shortcuts import render
from .forms import ClientForm, VehicleForm

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
            # Procesar los datos del formulario
            return redirect('success')
    else:
        client_form = ClientForm()
        vehicle_form = VehicleForm()
    return render(request, 'cliente/client_register.html', {'client_form': client_form, 'vehicle_form': vehicle_form})

def success_view(request):
    return render(request, 'cliente/success.html')