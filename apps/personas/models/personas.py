from django.db import models
from ..constants import GENERO_CHOICES


class Persona(models.Model):

    dni = models.CharField(max_length=8, verbose_name='DNI',
                           help_text='Escribe el DNI', unique=True)
    nombre = models.CharField(
        max_length=50, verbose_name='Nombre', help_text='Escribe el nombre')
    apellido = models.CharField(
        max_length=70, verbose_name='Apellido', help_text='Escribe los apellidos')
    fecha_nacimiento = models.DateField(null=True)
    correo = models.EmailField(max_length=100, verbose_name='Correo electrónico',
                               help_text='Escribe el correo electrónico', blank=True)
    genero = models.CharField(max_length=1, verbose_name='Género',
                              help_text='Selecciona el género', choices=GENERO_CHOICES)

    domicilio = models.ForeignKey('Domicilio', on_delete=models.CASCADE, verbose_name='Domicilio',
                                  help_text='Selecciona el domicilio', related_name='personas', blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Personas Fisicas"
        db_table = "personas_fisicas"

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
