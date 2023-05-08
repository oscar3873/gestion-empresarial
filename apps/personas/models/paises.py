from django.db import models


class Pais(models.Model):

    nombre = models.CharField(
        max_length=50, verbose_name='País', help_text='Escribe el país')

    class Meta:
        verbose_name_plural = "Países"
        db_table = "paises"

    def __str__(self):
        return '{}'.format(self.nombre)
