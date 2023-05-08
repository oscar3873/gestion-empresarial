from django import forms
from apps.personas.models.ciudades import Ciudad


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'