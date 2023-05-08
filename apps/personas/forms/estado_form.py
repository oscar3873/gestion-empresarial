from django import forms
from apps.personas.models.estados import Estado


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'