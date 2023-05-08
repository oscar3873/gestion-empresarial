from django.db import models


class TipoTelefono(models.Model):

    tipo = models.CharField(max_length=50, verbose_name='Tipo de teléfono',
                            help_text='Escribe el tipo de teléfono')

    class Meta:
        verbose_name_plural = "Tipos de teléfono"
        db_table = "tipos_telefono"

    def __str__(self):
        return '{}'.format(self.tipo)
