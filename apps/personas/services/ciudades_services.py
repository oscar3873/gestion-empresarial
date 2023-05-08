from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from apps.personas.models.ciudades import Ciudad
from apps.personas.services.estados_services import EstadoService


ESTADO_SERVICE = EstadoService()


class CiudadService:

    @transaction.atomic
    def crear_ciudad(self, datos_ciudad: dict):
        ciudad = Ciudad()
        ciudad.nombre = datos_ciudad['nombre']
        ciudad.estado = ESTADO_SERVICE.get_estado_by_id(datos_ciudad['estado'].id)
        ciudad.save()

    def get_ciudades(self):
        return Ciudad.objects.all()

    def get_ciudad_by_id(self, id):
        try:
            return Ciudad.objects.get(id=id)
        except Ciudad.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro una ciudad con el ID {}'.format(id))

    @transaction.atomic
    def editar_ciudad(self, id, datos_ciudad: dict):
        ciudad = self.get_ciudad_by_id(id)
        ciudad.nombre = datos_ciudad['nombre']
        ciudad.estado = ESTADO_SERVICE.get_estado_by_id(datos_ciudad['estado'].id)
        ciudad.save()

    @transaction.atomic
    def eliminar_ciudad(self, id):
        ciudad = self.get_ciudad_by_id(id)
        ciudad.delete()
