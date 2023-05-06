from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del departamento", help_text="Nombre del departamento", blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripción del departamento", help_text="Descripción del departamento", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"