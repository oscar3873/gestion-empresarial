from django.contrib import admin
from .models import Empleado, Departamento

admin.site.site_header = 'Empleados'


# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'salario', 'fecha_de_alta', 'created_at', 'update_at')
    list_filter = ('departamento', 'fecha_de_alta', 'salario')
    search_fields = ('nombre', 'apellido')
    ordering = ('id',)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'created_at', 'update_at')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('id',)