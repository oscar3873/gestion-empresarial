# importamos librerias para el uso de las vistas basadas en clases
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.personas.forms.persona_form import PersonaForm

from apps.personas.models.personas import Persona
from apps.personas.services.personas_services import PersonaService


# views de personas


class PersonaBaseView:
    model = Persona
    service = PersonaService()
    context_object_name = 'personas'

    def get_success_url(self):
        return reverse_lazy('personas:personas_list')


class PersonaList(PersonaBaseView, ListView):
    template_name = 'personas/persona/persona_list.html'

    def get_queryset(self):
        return self.service.get_personas().order_by('nombre', 'apellido')


class PersonaDetail(PersonaBaseView, DetailView):
    template_name = 'personas/persona/persona_detail.html'
    context_object_name = 'persona'

    def get_object(self, queryset=None):
        return self.service.get_persona_by_id(self.kwargs['pk'])


class PersonaCreate(PersonaBaseView, CreateView):
    form_class = PersonaForm
    template_name = 'personas/persona/persona_form.html'

    def form_valid(self, form):
        self.service.crear_persona(form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())


class PersonaUpdate(PersonaBaseView, UpdateView):
    form_class = PersonaForm
    template_name = 'personas/persona/persona_form.html'

    def get_object(self, queryset=None):
        return self.service.get_persona_by_id(self.kwargs['pk'])

    def form_valid(self, form):
        self.service.editar_persona(self.kwargs['pk'], form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())


class PersonaDelete(PersonaBaseView, DeleteView):
    template_name = 'personas/persona/persona_delete.html'
    context_object_name = 'persona'
    
    def get_object(self, queryset=None):
        return self.service.get_persona_by_id(self.kwargs['pk'])

    def form_valid(self, form):
        self.service.eliminar_persona(self.kwargs['pk'])
        return HttpResponseRedirect(self.get_success_url())
