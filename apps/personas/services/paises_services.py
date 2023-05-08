from apps.personas.models.paises import Pais
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


class PaisService:

    @transaction.atomic
    def crear_pais(self, datos_pais: dict):
        pais = Pais()
        pais.nombre = datos_pais['nombre']
        pais.save()

    def get_paises(self):
        return Pais.objects.all()

    def get_pais_by_id(self, id):
        try:
            return Pais.objects.get(id=id)
        except Pais.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un pais con el ID {}'.format(id))

    def get_pais_by_name(self, name):
        try:
            return Pais.objects.get(name=name)
        except Pais.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un pais con el nombre {}'.format(name))

    @transaction.atomic
    def editar_pais(self, id, datos_pais):
        pais = self.get_pais_by_id(id)
        pais.nombre = datos_pais['nombre']
        pais.save()

    @transaction.atomic
    def eliminar_pais(self, id):
        pais = self.get_pais_by_id(id)
        pais.delete()
