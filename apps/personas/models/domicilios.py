from django.db import models
from .personas import Persona
from .ciudades import Ciudad


class Domicilio(models.Model):

    calle = models.CharField(
        max_length=50, verbose_name='Calle', help_text='Escribe la calle')
    numero = models.CharField(
        max_length=10, verbose_name='Número', help_text='Escribe el número de domicilio')
    piso = models.CharField(
        max_length=10, verbose_name='Piso', help_text='Escribe el piso', blank=True)
    departamento = models.CharField(
        max_length=10, verbose_name='Departamento', help_text='Escribe el departamento', blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name='Ciudad',
                                  help_text='Selecciona la ciudad', related_name='domicilio')

    class Meta:
        verbose_name_plural = "Domicilios"
        db_table = "domicilios"

    def __str__(self):
        return '{} {} {} {} {} - {}, {}'.format(self.calle, self.numero, self.piso, self.departamento, self.ciudad, self.ciudad.estado, self.ciudad.estado.pais)
