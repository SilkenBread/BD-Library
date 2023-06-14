from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import EditorialForm
#from app.forms import AreaConocimientoForm
from app.models import *
from django.core import serializers
import json

class EditorialListView(ListView):
    model = Editorial
    template_name = 'editorial/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list_editorial':
                queryset = self.model.objects.all()
                data['type'] = 'success'
                data['data'] = serializers.serialize('json', queryset)
        except Exception as e:
            data['type'] = 'error'
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Editoriales'
        context['list_url'] = reverse_lazy('app:editorial_list')
        context['create_url'] = reverse_lazy('app:editorial_create')
        context['entity'] = 'Editoriales'
        return context


class EditorialCreateView(CreateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial/create.html'
    success_url = reverse_lazy('app:editorial_list')
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
        context['title'] = 'Creacion de una editorial'
        context['entity'] = 'Editoriales'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class EditorialUpdateView(UpdateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial/create.html'
    success_url = reverse_lazy('app:editorial_list')
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
    
class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'editorial/delete.html'
    success_url = reverse_lazy('app:editorial_list')
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