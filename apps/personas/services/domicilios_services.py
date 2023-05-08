from apps.personas.services.personas_services import PersonaService
from apps.personas.models.domicilios import Domicilio

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from apps.personas.services.ciudades_services import CiudadService


CIUDAD_SERVICE = CiudadService()
PERSONA_SERVICE = PersonaService()


class DomicilioService:

    @transaction.atomic
    def crear_domicilio(self, datos_domicilio: dict):
        domicilio = Domicilio()
        self._crear_o_actualizar_domicilio(domicilio, datos_domicilio)
        domicilio.save()

    def get_domicilios(self):
        domicilios = Domicilio.objects.all()
        return domicilios

    def get_domicilio_by_id(self, id):
        try:
            return Domicilio.objects.get(id=id)
        except Domicilio.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un domicilio con el ID {}'.format(id))

    @transaction.atomic
    def editar_domicilio(self, id, datos_domicilio: dict):
        domicilio = self.get_domicilio_by_id(id)
        self._crear_o_actualizar_domicilio(domicilio, datos_domicilio)
        domicilio.save()

    @transaction.atomic
    def eliminar_domicilio(self, id):
        domicilio = self.get_domicilio_by_id(id)
        domicilio.delete()
        
    def _crear_o_actualizar_domicilio(self, domicilio, datos_domicilio: dict):
        domicilio.calle = datos_domicilio['calle']
        domicilio.numero = datos_domicilio['numero']
        domicilio.piso = datos_domicilio['piso']
        domicilio.departamento = datos_domicilio['departamento']
        domicilio.ciudad = CIUDAD_SERVICE.get_ciudad_by_id(
            datos_domicilio['ciudad'].id)
