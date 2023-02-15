from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'App_Servicios/index.html')


def servicios(request):
    return HttpResponse('SERVICIOS')


def clientes(request):
    return HttpResponse('CLIENTES')


def activos(request):
    return HttpResponse('ACTIVOS')


def empleados(request):
    return HttpResponse('EMPLEADOS')