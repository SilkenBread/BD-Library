from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from app.forms import AutorForm
#from app.forms import Autor
from app.models import *
from django.core import serializers
import json

class AutoresListView(ListView):
    model = Autor
    template_name = 'autor/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list_autores':
                queryset = self.model.objects.all()
                data['type'] = 'success'
                data['data'] = serializers.serialize('json', queryset)

        except Exception as e:
            data['type'] = 'error'
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Autores'
        context['list_url'] = reverse_lazy('app:autores_list')
        context['create_url'] = reverse_lazy('app:autores_create')
        context['entity'] = 'Autores'
        return context
    
class AutoresCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/create.html'
    success_url = reverse_lazy('app:autores_list')
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
        context['title'] = 'Creacion de Autores'
        context['entity'] = 'Autores'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context