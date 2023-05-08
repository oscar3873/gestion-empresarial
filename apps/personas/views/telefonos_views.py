from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.personas.forms.telefono_form import TelefonoForm
from apps.personas.models.telefonos import Telefono
from apps.personas.services.telefonos_services import TelefonoService

 
class TelefonoBaseView:
    model = Telefono
    service = TelefonoService()
    context_object_name = 'telefonos'

    def get_success_url(self):
        return reverse_lazy('personas:telefonos_list')
    
class TelefonoList(TelefonoBaseView, ListView):
    template_name = 'personas/telefono/telefono_list.html'
    ordering = ['cod_area']
    def get_queryset(self):
        return self.service.get_telefonos().order_by('persona__nombre', 'persona__apellido', 'tipo')
    

class TelefonoDetail(TelefonoBaseView, DetailView):
    template_name = 'personas/telefono/telefono_detail.html'
    context_object_name = 'telefono'
    
    def get_object(self, queryset=None):
        return self.service.get_telefono_by_id(self.kwargs['pk'])
    

class TelefonoUpdate(TelefonoBaseView, UpdateView):
    form_class = TelefonoForm
    template_name = 'personas/telefono/telefono_form.html'
    
    def get_object(self, queryset=None):
        return self.service.get_telefono_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.editar_telefono(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())

class TelefonoCreate(TelefonoBaseView, CreateView):
    form_class = TelefonoForm
    template_name = 'personas/telefono/telefono_form.html'
    
    def form_valid(self, form):
        self.service.crear_telefono(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
        
class TelefonoDelete(TelefonoBaseView, DeleteView):
    template_name = 'personas/telefono/telefono_delete.html'
    context_object_name = 'telefono'
    
    def get_object(self, queryset=None):
        return self.service.get_telefono_by_id(self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse_lazy('personas:telefonos_list')