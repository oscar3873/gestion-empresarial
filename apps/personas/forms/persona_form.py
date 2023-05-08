from django.forms import ModelForm
from apps.personas.models.personas import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
