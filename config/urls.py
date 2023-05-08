from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('personas/', include('apps.personas.urls')),
    path('admin/', admin.site.urls),
    # Agrega tus otras rutas aquí
]
