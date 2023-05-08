from django.db import models
from .paises import Pais


class Estado(models.Model):

    estado = models.CharField(
        max_length=50, verbose_name='Estado/Provincia', help_text='Escribe el estado/provincia')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name='País',
                             help_text='Selecciona el país', related_name='estados')

    class Meta:
        verbose_name_plural = "Estados/Provincias"
        db_table = "estados_provincias"

    def __str__(self):
        return '{}'.format(self.estado)
