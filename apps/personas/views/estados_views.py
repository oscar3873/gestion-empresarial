from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.personas.forms.estado_form import EstadoForm

from apps.personas.models.estados import Estado
from apps.personas.services.estados_services import EstadoService

# views de estados

class EstadoBaseView:
    model = Estado
    service = EstadoService()
    context_object_name = 'estados'

    def get_success_url(self):
        return reverse_lazy('personas:estados_list')
    

class EstadoList(EstadoBaseView, ListView):
    template_name = 'personas/estado/estado_list.html'

    def get_queryset(self):
        return self.service.get_estados().order_by('estado')
    

class EstadoDetail(EstadoBaseView, DetailView):
    template_name = 'personas/estado/estado_detail.html'
    context_object_name = 'estado'

    def get_object(self, queryset=None):
        return self.service.get_estado_by_id(self.kwargs['pk'])
    

class EstadoCreate(EstadoBaseView, CreateView):
    form_class = EstadoForm
    template_name = 'personas/estado/estado_form.html'

    def form_valid(self, form):
        self.service.crear_estado(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    
    
class EstadoUpdate(EstadoBaseView, UpdateView):
    form_class = EstadoForm
    template_name = 'personas/estado/estado_form.html'

    def get_object(self, queryset=None):
        return self.service.get_estado_by_id(self.kwargs['pk'])

    def form_valid(self, form):
        self.service.editar_estado(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
    

class EstadoDelete(EstadoBaseView, DeleteView):
    template_name = 'personas/estado/estado_delete.html'
    context_object_name = 'estado'
    
    def get_object(self, queryset=None):
        return self.service.get_estado_by_id(self.kwargs['pk'])
    
    def form_valid(self, form):
        self.service.eliminar_estado(self.kwargs['pk'])
        return HttpResponseRedirect(self.get_success_url())