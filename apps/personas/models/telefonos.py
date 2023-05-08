from django.db import models
from ..constants import COD_PAISES, MAX_COD_PAIS_LENGTH
from .personas import Persona
from .tipo_telefonos import TipoTelefono


class Telefono(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='telefonos',
                                verbose_name='Persona', help_text='Selecciona la persona')
    cod_pais = models.CharField(max_length=MAX_COD_PAIS_LENGTH, verbose_name='Código de país',
                                help_text='Selecciona el código de país', choices=COD_PAISES, blank=True)
    cod_area = models.CharField(max_length=5, verbose_name='Código de área',
                                help_text='Escribe el código de área', blank=True)
    numero = models.CharField(
        max_length=9, verbose_name='Número', help_text='Escribe el número de teléfono')
    tipo = models.ForeignKey(TipoTelefono, on_delete=models.CASCADE, verbose_name='Tipo de teléfono',
                             help_text='Selecciona el tipo de teléfono', related_name='telefonos')

    @property
    def nombre_cod_pais(self):
        for pais in COD_PAISES:
            if pais[0] == self.cod_pais:
                return pais[1]
        return ''

    class Meta:
        verbose_name_plural = "Teléfonos"
        db_table = "telefonos"

    def __str__(self):
        return '+{} {} {}'.format(self.cod_pais, self.cod_area, self.numero)
