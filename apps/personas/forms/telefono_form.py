#importaciones de django para formularios y formularios en linea
from django.forms import ModelForm
from django.forms import inlineformset_factory
from apps.personas.models.personas import Persona
from apps.personas.models.telefonos import Telefono


class TelefonoForm(ModelForm):
    class Meta:
        model = Telefono
        fields = "__all__"
        
TelefonoFormSet = inlineformset_factory(Persona, Telefono, form=TelefonoForm, extra=1)
