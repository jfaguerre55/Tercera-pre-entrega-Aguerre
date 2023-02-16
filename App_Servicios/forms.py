from django import forms

class FormularioServicios(forms.Form):

    nombre = forms.CharField()
    area = forms.CharField()
    fecha_alta = forms.DateField()
    activo = forms.BooleanField()


class FormularioClientes(forms.Form):
    
    nombre = forms.CharField()
    cuit = forms.IntegerField()
    fecha_alta = forms.DateField()
    domicilio = forms.CharField()
    mail = forms.EmailField()


class FormularioActivos(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    categoria = forms.CharField()
    fecha_alta = forms.DateField()
    descripcion = forms.CharField()


class FormularioEmpleados(forms.Form):
    
    nombre = forms.CharField()
    edad = forms.IntegerField()
    legajo = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    mail = forms.EmailField()




