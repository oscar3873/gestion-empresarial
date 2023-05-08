from django import forms
from apps.personas.models.domicilios import Domicilio


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'