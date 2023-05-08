from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.personas.forms.domicilio_form import DomicilioForm

from apps.personas.models.domicilios import Domicilio
from apps.personas.services.domicilios_services import DomicilioService

#views de domicilios

class DomicilioBaseView:
    model = Domicilio
    service = DomicilioService()
    context_object_name = 'domicilios'

    def get_success_url(self):
        return reverse_lazy('personas:domicilios_list')
    

class DomicilioList(DomicilioBaseView, ListView):
    template_name = 'personas/domicilio/domicilio_list.html'

    def get_queryset(self):
        return self.service.get_domicilios().order_by('calle', 'numero')
    
    
class DomicilioDetail(DomicilioBaseView, DetailView):
    template_name = 'personas/domicilio/domicilio_detail.html'
    context_object_name = 'domicilio'

    def get_object(self, queryset=None):
        return self.service.get_domicilio_by_id(self.kwargs['pk'])
    

class DomicilioCreate(DomicilioBaseView, CreateView):
    form_class = DomicilioForm
    template_name = 'personas/domicilio/domicilio_form.html'

    def form_valid(self, form):
        self.service.crear_domicilio(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
   
    
class DomicilioUpdate(DomicilioBaseView, UpdateView):
    form_class = DomicilioForm
    template_name = 'personas/domicilio/domicilio_form.html'

    def get_object(self, queryset=None):
        return self.service.get_domicilio_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.editar_domicilio(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class DomicilioDelete(DomicilioBaseView, DeleteView):
    template_name = 'personas/domicilio/domicilio_delete.html'

    def get_object(self, queryset=None):
        return self.service.get_domicilio_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.eliminar_domicilio(self.kwargs['pk'])
        return HttpResponseRedirect(self.get_success_url())