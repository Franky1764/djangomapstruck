from django.shortcuts import render

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