from apps.personas.models import Persona
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


class PersonaService():

    """Create de la tabla Personas"""
    @transaction.atomic
    def crear_persona(self, datos_persona):
        """Datos de persona tiene que ser un diccionario con los campos de la tabla Personas"""
        persona = Persona()
        self._crear_o_actualizar_persona(persona, datos_persona)
        persona.save()

    def get_personas(self):
        personas = Persona.objects.all()
        return personas

    def get_persona_by_id(self, id):
        try:
            return Persona.objects.get(id=id)
        except Persona.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro una persona con el ID {}'.format(id))

    def get_persona_by_correo(self, correo):
        try:
            return Persona.objects.get(correo=correo)
        except Persona.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro una persona con el email {}'.format(correo))

    def get_persona_by_dni(self, dni):
        try:
            return Persona.objects.get(dni=dni)
        except Persona.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro una persona con el dni {}'.format(dni))

    """Update de la tabla Personas"""
    @transaction.atomic
    def editar_persona(self, id, datos_persona):
        """Datos de persona tiene que ser un diccionario con los campos de la tabla Personas"""
        persona = self.get_persona_by_id(id)
        self._crear_o_actualizar_persona(persona, datos_persona)
        persona.save()

    """Delete de la tabla Personas"""
    @transaction.atomic 
    def eliminar_persona(self, id):
        persona = self.get_persona_by_id(id)
        persona.delete()

    """
    Metodos privados de la clase TelefonoService
    """

    def _crear_o_actualizar_persona(self, persona, datos_persona: dict):
        persona.domicilio = datos_persona['domicilio']
        persona.dni = datos_persona['dni']
        persona.nombre = datos_persona['nombre']
        persona.apellido = datos_persona['apellido']
        persona.fecha_nacimiento = datos_persona['fecha_nacimiento']
        persona.correo = datos_persona['correo']
        persona.genero = datos_persona['genero']