from django import forms
from RApp2.models import Proyecto, Etiqueta


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_limite': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
