
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from apps.personas.models.telefonos import Telefono
from apps.personas.services.tipo_telefonos_services import TipoTelefonoService
from apps.personas.services.personas_services import PersonaService


PERSONA_SERVICE = PersonaService()
TIPO_TELEFONO_SERVICE = TipoTelefonoService()


class TelefonoService:

    @transaction.atomic
    def crear_telefono(self, datos_telefono: dict):
        telefono = Telefono()
        self._crear_o_actualizar_telefono(telefono, datos_telefono)
        telefono.save()
                
    def get_telefonos(self):
        telefono = Telefono.objects.all()
        return telefono

    def get_telefono_by_id(self, id: int):
        try:
            return Telefono.objects.get(id=id)
        except Telefono.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un teléfono con el ID {}'.format(id))

    @transaction.atomic
    def editar_telefono(self, id: int, datos_telefono: dict):
        telefono = self.get_telefono_by_id(id)
        self._crear_o_actualizar_telefono(telefono, datos_telefono)
        telefono.save()

    @transaction.atomic
    def eliminar_telefono(self, id: int):
        telefono = self.get_telefono_by_id(id)
        telefono.delete()
        
    """
    Metodos privados de la clase TelefonoService
    """
    
    def _crear_o_actualizar_telefono(self, telefono, datos_telefono: dict):
        telefono.persona = PERSONA_SERVICE.get_persona_by_id(
            datos_telefono['persona'].id)
        telefono.cod_pais = datos_telefono['cod_pais']
        telefono.cod_area = datos_telefono['cod_area']
        telefono.numero = datos_telefono['numero']
        telefono.tipo = TIPO_TELEFONO_SERVICE.get_tipo_telefono_by_id(
            datos_telefono['tipo'].id)
