# urls de personas
from django.urls import path
from apps.personas.views.personas_views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete, PersonaDetail
from apps.personas.views.telefonos_views import TelefonoList, TelefonoCreate, TelefonoUpdate, TelefonoDelete, TelefonoDetail
from apps.personas.views.domicilios_views import DomicilioList, DomicilioCreate, DomicilioUpdate, DomicilioDelete, DomicilioDetail
from apps.personas.views.ciudades_views import CiudadList, CiudadCreate, CiudadUpdate, CiudadDelete, CiudadDetail
from apps.personas.views.estados_views import EstadoList, EstadoCreate, EstadoUpdate, EstadoDelete, EstadoDetail
from apps.personas.views.paises_views import PaisList, PaisCreate, PaisUpdate, PaisDelete, PaisDetail

app_name = 'personas'
urlpatterns = [
    path('personas/list/', PersonaList.as_view(), name='personas_list'),
    path('personas/create/', PersonaCreate.as_view(), name='personas_create'),
    path('personas/update/<int:pk>/', PersonaUpdate.as_view(), name='personas_update'),
    path('personas/delete/<int:pk>/', PersonaDelete.as_view(), name='personas_delete'),
    path('personas/detail/<int:pk>/', PersonaDetail.as_view(), name='personas_detail'),
    
    path('telefonos/list/', TelefonoList.as_view(), name='telefonos_list'),
    path('telefonos/create/', TelefonoCreate.as_view(), name='telefonos_create'),
    path('telefonos/update/<int:pk>/', TelefonoUpdate.as_view(), name='telefonos_update'),
    path('telefonos/delete/<int:pk>/', TelefonoDelete.as_view(), name='telefonos_delete'),
    path('telefonos/detail/<int:pk>/', TelefonoDetail.as_view(), name='telefonos_detail'),
    
    path('domicilios/list/', DomicilioList.as_view(), name='domicilios_list'),
    path('domicilios/create/', DomicilioCreate.as_view(), name='domicilios_create'),
    path('domicilios/update/<int:pk>/', DomicilioUpdate.as_view(), name='domicilios_update'),
    path('domicilios/delete/<int:pk>/', DomicilioDelete.as_view(), name='domicilios_delete'),
    path('domicilios/detail/<int:pk>/', DomicilioDetail.as_view(), name='domicilios_detail'),
    
    path('ciudades/list/', CiudadList.as_view(), name='ciudades_list'),
    path('ciudades/create/', CiudadCreate.as_view(), name='ciudades_create'),
    path('ciudades/update/<int:pk>/', CiudadUpdate.as_view(), name='ciudades_update'),
    path('ciudades/delete/<int:pk>/', CiudadDelete.as_view(), name='ciudades_delete'),
    path('ciudades/detail/<int:pk>/', CiudadDetail.as_view(), name='ciudades_detail'),
    
    path('estados/list/', EstadoList.as_view(), name='estados_list'),
    path('estados/create/', EstadoCreate.as_view(), name='estados_create'),
    path('estados/update/<int:pk>/', EstadoUpdate.as_view(), name='estados_update'),
    path('estados/delete/<int:pk>/', EstadoDelete.as_view(), name='estados_delete'),
    path('estados/detail/<int:pk>/', EstadoDetail.as_view(), name='estados_detail'),
    
    path('paises/list/', PaisList.as_view(), name='paises_list'),
    path('paises/create/', PaisCreate.as_view(), name='paises_create'),
    path('paises/update/<int:pk>/', PaisUpdate.as_view(), name='paises_update'),
    path('paises/delete/<int:pk>/', PaisDelete.as_view(), name='paises_delete'),
    path('paises/detail/<int:pk>/', PaisDetail.as_view(), name='paises_detail'),
]
