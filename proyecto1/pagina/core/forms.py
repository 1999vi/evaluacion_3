from django import forms
from django.forms import ModelForm, widgets
from .models import Obra

class obraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['autor', 'nombre', 'descripcion', 'historia', 'tecnica', 'precio', 'imagen', 'concepto']
        widgets={
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'historia': forms.TextInput(attrs={'class': 'form-control'}),
            'tecnica': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'concepto': forms.Select(attrs={'class': 'form-control'}),
        }