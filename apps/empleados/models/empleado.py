from django.db import models
from .departamento import Departamento

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del empleado", help_text="Nombre del empleado", blank=True, null=True)
    apellido = models.CharField(max_length=100, verbose_name="Apellido del empleado", help_text="Apellido del empleado", blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario del empleado", help_text="Salario del empleado")
    fecha_de_alta = models.DateField(verbose_name="Fecha de alta del empleado", help_text="Fecha de alta del empleado", default="2020-01-01")
    
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento", help_text="Departamento", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
