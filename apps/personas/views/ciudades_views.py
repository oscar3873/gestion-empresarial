from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.personas.forms.ciudad_form import CiudadForm

from apps.personas.models.ciudades import Ciudad
from apps.personas.services.ciudades_services import CiudadService

# views de ciudades

class CiudadBaseView:
    model = Ciudad
    service = CiudadService()
    context_object_name = 'ciudades'

    def get_success_url(self):
        return reverse_lazy('personas:ciudades_list')
   

class CiudadList(CiudadBaseView, ListView):
    template_name = 'personas/ciudad/ciudad_list.html'

    def get_queryset(self):
        return self.service.get_ciudades().order_by('nombre')
    

class CiudadDetail(CiudadBaseView, DetailView):
    template_name = 'personas/ciudad/ciudad_detail.html'
    context_object_name = 'ciudad'

    def get_object(self, queryset=None):
        return self.service.get_ciudad_by_id(self.kwargs['pk'])
    
    
class CiudadCreate(CiudadBaseView, CreateView):
    form_class = CiudadForm
    template_name = 'personas/ciudad/ciudad_form.html'

    def form_valid(self, form):
        self.service.crear_ciudad(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class CiudadUpdate(CiudadBaseView, UpdateView):
    form_class = CiudadForm
    template_name = 'personas/ciudad/ciudad_form.html'

    def get_object(self, queryset=None):
        return self.service.get_ciudad_by_id(self.kwargs['pk'])

    def form_valid(self, form):
        self.service.editar_ciudad(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class CiudadDelete(CiudadBaseView, DeleteView):
    template_name = 'personas/ciudad/ciudad_delete.html'
    context_object_name = 'ciudad'
    
    def get_object(self, queryset=None):
        return self.service.get_ciudad_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.eliminar_ciudad(self.kwargs['pk'])
        return HttpResponseRedirect(self.get_success_url())