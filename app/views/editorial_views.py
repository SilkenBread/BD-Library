from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import EditorialForm
from app.mixins import ValidatePermissionRequiredMixin
from app.models import *
from django.core import serializers
import json

class EditorialListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Editorial
    template_name = 'editorial/list.html'
    permission_required = 'app.view_editorial'

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


class EditorialCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial/create.html'
    success_url = reverse_lazy('app:editorial_list')
    permission_required = 'app.add_editorial'
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
    
class EditorialUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial/create.html'
    permission_required = 'app.change_editorial'
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
        context['title'] = 'Edición de una Editorial'
        context['entity'] = 'Editoriales'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    
class EditorialDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Editorial
    template_name = 'editorial/delete.html'
    permission_required = 'app.delete_editorial'
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
        context['title'] = 'Eliminación de una editorial'
        context['entity'] = 'Editoriales'
        context['list_url'] = self.success_url
        return context