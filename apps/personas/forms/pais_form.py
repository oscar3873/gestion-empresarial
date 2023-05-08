from django import forms
from apps.personas.models.paises import Pais


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'