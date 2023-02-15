
from django.urls import path

from App_Servicios.views import *

urlpatterns = [
    path('', index, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('clientes/', clientes, name='clientes'),
    path('activos/', activos, name='activos'),
    path('empleados/', empleados, name='empleados')
]
