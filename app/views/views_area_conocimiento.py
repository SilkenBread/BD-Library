
from django.http import JsonResponse
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from app.models import Areaconocimiento
from django.core import serializers
from django.urls import reverse_lazy

class AreaConocimientoListView(ListView):
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

            if action == 'delete_area_conocimiento':
                try:
                    codigo_area = request.POST.get('parameters')
                    area = Areaconocimiento.objects.get(codigo_area=codigo_area)
                    area.delete()
                    data['type']='success'
                    data['msg']= 'Se eliminó el área de conocimiento correctamente.'
                except Areaconocimiento.DoesNotExist:
                    raise ValueError("No es posible eliminar esta area")

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
    
class AreaConocimientoCreateView(TemplateView):
    model = Areaconocimiento
    template_name = 'area_conocimiento/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion área de conocimiento'
        context['list_url'] = reverse_lazy('app:area_conocimiento_list')
        context['create_url'] = reverse_lazy('app:area_conocimiento_create')
        context['entity'] = 'Creacion área de conocimiento'
        return context