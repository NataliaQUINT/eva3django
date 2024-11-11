# core/views.py

from django.shortcuts import render
# Create your views here.

def main(request):
    return render(request, 'core/main.html')

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def formulario(request):
    return render(request, 'core/formulario.html')
def login(request):
    return render(request, 'core/login.html')

def error(request):
    return render(request, 'core/error.html')

def planes(request):
    return render(request, 'core/planes.html')

def registro(request):
    return render(request, 'core/registro.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def transporte(request):
    return render(request, 'core/transporte.html')

def lugares(request):
    return render(request, 'core/lugares.html')

def hospital_details(request):
    return render(request, 'core/hospital.html')  # Página del hospital

def comisaria_details(request):
    return render(request, 'core/comisaria.html')  # Página de la comisaría




