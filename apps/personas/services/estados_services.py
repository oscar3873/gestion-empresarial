from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from apps.personas.models.estados import Estado
from apps.personas.services.paises_services import PaisService


PAIS_SERVICE = PaisService()


class EstadoService:

    @transaction.atomic
    def crear_estado(self, datos_estado: dict):
        estado = Estado()
        estado.estado = datos_estado['estado']
        estado.pais = PAIS_SERVICE.get_pais_by_id(datos_estado['pais'].id)
        estado.save()

    def get_estados(self):
        return Estado.objects.all()

    def get_estado_by_id(self, id):
        try:
            return Estado.objects.get(id=id)
        except Estado.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un estado con el ID {}'.format(id))

    @transaction.atomic
    def editar_estado(self, id, datos_estado):
        estado = self.get_estado_by_id(id)
        estado.estado = datos_estado['estado']
        estado.pais = estado.pais = PAIS_SERVICE.get_pais_by_id(
            datos_estado['pais'].id)
        estado.save()

    @transaction.atomic
    def eliminar_estado(self, id):
        estado = self.get_estado_by_id(id)
        estado.delete()
