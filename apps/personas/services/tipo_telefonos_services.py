from ..models import TipoTelefono
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


class TipoTelefonoService:

    @transaction.atomic
    def crear_tipo_telefono(self, datos_tipo_telefono: dict):
        """
        Usamos esta forma aqui **datos_tipo_telefono porque no tenemos
        que validar los datos, con nuestra rutina de validacion de datos.
        """
        TipoTelefono.objects.create(**datos_tipo_telefono)

    def get_tipos_telefono(self):
        return TipoTelefono.objects.all()

    def get_tipo_telefono_by_id(self, id: int):
        try:
            return TipoTelefono.objects.get(id=id)
        except TipoTelefono.DoesNotExist:
            raise ObjectDoesNotExist(
                'No se encontro un tipo de telefono con el ID {}'.format(id))

    @transaction.atomic
    def actualizar_tipo_telefono(self, id: int, datos_tipo_telefono: dict):
        """
        Dejamos esta forma y no la forma con **datos_tipo_telefono porque
        asi tenemos control sobre que campos se pueden actualizar con nuestra
        rutina de validacion de datos.
        """
        tipo_telefono = self.get_tipo_telefono_by_id(id)
        tipo_telefono.tipo = datos_tipo_telefono['tipo']
        tipo_telefono.save()

    @transaction.atomic
    def eliminar_tipo_telefono(self, id: int):
        tipo_telefono = self.get_tipo_telefono_by_id(id)
        tipo_telefono.delete()
