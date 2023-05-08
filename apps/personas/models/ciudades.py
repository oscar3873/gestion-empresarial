from django.db import models
from .estados import Estado


class Ciudad(models.Model):

    nombre = models.CharField(
        max_length=50, verbose_name='Ciudad', help_text='Escribe la ciudad')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='Estado',
                               help_text='Selecciona el estado', related_name='ciudades', default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ciudades"
        db_table = "ciudades"

    def __str__(self):
        return '{}'.format(self.nombre)
