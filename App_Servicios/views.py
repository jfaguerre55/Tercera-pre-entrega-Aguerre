from django.shortcuts import render, redirect
from django.http import HttpResponse

from App_Servicios.models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'App_Servicios/index.html')


def servicios(request):
    if request.method == 'POST':
        mi_form = FormularioServicios(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            new_servicio= Servicio(name=info['nombre'], area=info['area'], fecha_alta=info['fecha_alta'], estado=info['activo'])
            new_servicio.save()
            return redirect('inicio')
    else:
        mi_form = FormularioServicios()

    return render(request, 'App_Servicios/servicios.html', {"formulario_servicio":mi_form})



def clientes(request):
    if request.method == 'POST':
        mi_form = FormularioClientes(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            new_cliente = Cliente(name=info['nombre'], cuit=info['cuit'], fecha_alta=info['fecha_alta'], domicilio=info['domicilio'], mail=info['mail'])
            new_cliente.save()
            return redirect('inicio')
    else:
        mi_form = FormularioClientes()

    return render(request, 'App_Servicios/clientes.html', {"formulario_cliente":mi_form})

    

def activos(request):
    if request.method == 'POST':
        mi_form = FormularioActivos(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            new_activo = Activo(name=info['nombre'], categoria=info['categoria'], fecha_alta=info['fecha_alta'], descripcion=info['descripcion'])
            new_activo.save()
            return redirect('inicio')
    else:
        mi_form = FormularioActivos()

    return render(request, 'App_Servicios/activos.html', {"formulario_activo":mi_form})



def empleados(request):
    if request.method == 'POST':
        mi_form = FormularioEmpleados(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            new_empleado = Empleado(name=info['nombre'], age=info['edad'], legajo=info['legajo'], fecha_nac=info['fecha_nacimiento'], mail=info['mail'])
            new_empleado.save()
            return redirect('inicio')
    else:
        mi_form = FormularioEmpleados()
    
    return render(request, 'App_Servicios/empleados.html', {"formulario_empleado":mi_form})
