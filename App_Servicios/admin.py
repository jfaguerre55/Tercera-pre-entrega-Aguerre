from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Activo)
admin.site.register(Empleado)