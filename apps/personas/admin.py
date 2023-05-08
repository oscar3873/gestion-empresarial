from django.contrib import admin

from .models import Persona, Telefono, TipoTelefono, Domicilio, Ciudad, Pais, Estado


class TelefonoInline(admin.TabularInline):
    """Clase para poder enlazarla al admin y poder agregar teléfonos desde el admin de personas."""
    model = Telefono
    extra = 1


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    """Admin de la clase Persona."""

    inlines = [TelefonoInline]
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'correo', 'genero', 'telefonos', 'domicilio')
    list_filter = ('genero', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'dni')

    def telefonos(self, obj):
        """Devuelve la lista de números de teléfono de la persona."""
        return [t for t in obj.telefonos.all()]


@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    """Admin de la clase Telefono."""

    list_display = ('telefono', 'tipo', 'persona')
    list_filter = ('persona', 'tipo')
    search_fields = ('numero', 'persona__nombre', 'persona__apellido', 'persona__dni')

    def telefono(self, obj):
        """Devuelve el número de teléfono completo."""
        return obj


@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    """Admin de la clase Domicilio."""

    list_display = ('domicilio', 'estado', 'pais')
    search_fields = ('calle', 'numero',)

    def domicilio(self, obj):
        """Devuelve el domicilio completo."""
        return obj

    def estado(self, obj):
        """Devuelve el estado de la ciudad del domicilio."""
        return obj.ciudad.estado

    def pais(self, obj):
        """Devuelve el país del domicilio."""
        return obj.ciudad.estado.pais


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    """Admin de la clase Estado."""

    list_display = ('estado', 'pais')
    list_filter = ('pais',)


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    """Admin de la clase Ciudad."""
    pass


@admin.register(TipoTelefono)
class TipoTelefonoAdmin(admin.ModelAdmin):
    """Admin de la clase TipoTelefono."""
    pass


admin.site.site_header = 'Administración de Personas'
admin.site.register(Pais)
