from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import LibroForm
from app.mixins import ValidatePermissionRequiredMixin
from app.models import *
from django.core import serializers
import json

class LibroListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Libro
    template_name = 'libro/list.html'
    permission_required = 'app.view_libro'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list_libro':
                queryset = self.model.objects.all()
                data['type'] = 'success'
                data['data'] = serializers.serialize('json', queryset)

        except Exception as e:
            data['type'] = 'error'
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Libros'
        context['list_url'] = reverse_lazy('app:libro_list')
        context['create_url'] = reverse_lazy('app:libro_create')
        context['entity'] = 'Libros'
        return context
    
class LibroCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/create.html'
    permission_required = 'app.add_libro'
    success_url = reverse_lazy('app:libro_list')
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
        context['title'] = 'Creacion de un Libro'
        context['entity'] = 'Libros'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class LibroUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/create.html'
    permission_required = 'app.change_libro'
    success_url = reverse_lazy('app:libro_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                self.object = self.get_object()  # Obtener el objeto a actualizar
                form = self.get_form()
                if form.is_valid():
                    form.save()  # Guardar los cambios en el objeto existente
                    data['success'] = 'Registro actualizado exitosamente'
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un libro'
        context['entity'] = 'Libros'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    
class LibroDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Libro
    template_name = 'libro/delete.html'
    permission_required = 'app.delete_libro'
    success_url = reverse_lazy('app:libro_list')
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
        context['title'] = 'Eliminación de un libro'
        context['entity'] = 'Libros'
        context['list_url'] = self.success_url
        return context