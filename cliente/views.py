from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'cliente/index.html')

def nosotros (request):
    return render(request, 'cliente/nosotros.html')

def servicios(request):
    return render(request, 'cliente/servicios.html')

def contacto(request):
    return render(request, 'cliente/contacto.html')