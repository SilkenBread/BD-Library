from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import AreaConocimientoForm
from app.models import *
from django.core import serializers
import json

class AreaConocimientoListView(LoginRequiredMixin, ListView):
    model = Areaconocimiento
    template_name = 'area_conocimiento/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list_area_conocimiento':
                queryset = self.model.objects.all()
                data['type'] = 'success'
                data['data'] = serializers.serialize('json', queryset)

        except Exception as e:
            data['type'] = 'error'
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado áreas de conocimiento'
        context['list_url'] = reverse_lazy('app:area_conocimiento_list')
        context['create_url'] = reverse_lazy('app:area_conocimiento_create')
        context['entity'] = 'Áreas de conocimiento'
        return context

class AreaConocimientoCreateView(LoginRequiredMixin, CreateView):
    model = Areaconocimiento
    form_class = AreaConocimientoForm
    template_name = 'area_conocimiento/create.html'
    success_url = reverse_lazy('app:area_conocimiento_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un área de conocimiento'
        context['entity'] = 'Áreas de conocimiento'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class AreaConocimientoUpdateView(LoginRequiredMixin, UpdateView):
    model = Areaconocimiento
    form_class = AreaConocimientoForm
    template_name = 'area_conocimiento/create.html'
    success_url = reverse_lazy('app:area_conocimiento_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un área de conocimiento'
        context['entity'] = 'Áreas de conocimiento'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    
class AreaConocimientoDeleteView(LoginRequiredMixin, DeleteView):
    model = Areaconocimiento
    template_name = 'area_conocimiento/delete.html'
    success_url = reverse_lazy('app:area_conocimiento_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un área de conocimiento'
        context['entity'] = 'Áreas de conocimiento'
        context['list_url'] = self.success_url
        return context