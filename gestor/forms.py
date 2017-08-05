from django import forms
from .models import *
from django.forms.extras.widgets import SelectDateWidget

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('cliente','fecha','costo',)

class FechaForm(forms.ModelForm):
    dato_fecha = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Fecha
        fields = ('dato_fecha',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('nombre', 'apellidos','cedula',)

class FiltroForm(forms.Form):
    inicio_fecha = forms.DateField(widget=SelectDateWidget)
    inicio_fin = forms.DateField(widget=SelectDateWidget)
