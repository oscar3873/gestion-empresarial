from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.personas.forms.pais_form import PaisForm

from apps.personas.models.paises import Pais
from apps.personas.services.paises_services import PaisService

# views de paises

class PaisBaseView:
    model = Pais
    service = PaisService()
    context_object_name = 'paises'

    def get_success_url(self):
        return reverse_lazy('personas:paises_list')
    

class PaisList(PaisBaseView, ListView):
    template_name = 'personas/pais/pais_list.html'

    def get_queryset(self):
        return self.service.get_paises().order_by('nombre')
    

class PaisDetail(PaisBaseView, DetailView):
    template_name = 'personas/pais/pais_detail.html'
    context_object_name = 'pais'

    def get_object(self, queryset=None):
        return self.service.get_pais_by_id(self.kwargs['pk'])
    

class PaisCreate(PaisBaseView, CreateView):
    form_class = PaisForm
    template_name = 'personas/pais/pais_form.html'

    def form_valid(self, form):
        self.service.crear_pais(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class PaisUpdate(PaisBaseView, UpdateView):
    form_class = PaisForm
    template_name = 'personas/pais/pais_form.html'

    def get_object(self, queryset=None):
        return self.service.get_pais_by_id(self.kwargs['pk'])

    def form_valid(self, form):
        self.service.editar_pais(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class PaisDelete(PaisBaseView, DeleteView):
    template_name = 'personas/pais/pais_delete.html'
    context_object_name = 'pais'
    
    def get_object(self, queryset=None):
        return self.service.get_pais_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.eliminar_pais(self.kwargs['pk'])
        return HttpResponseRedirect(self.get_success_url())