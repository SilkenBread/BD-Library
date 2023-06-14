from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
#from app.forms import AreaConocimientoForm
from app.models import *
from django.core import serializers
import json

class LibroListView(ListView):
    model = Libro
    template_name = 'libro/list.html'

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