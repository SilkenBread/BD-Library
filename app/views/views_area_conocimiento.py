
from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.models import Areaconocimiento


class AreaConocimientoListView(ListView):
    model = Areaconocimiento
    template_name = 'area_conocimiento/list.html'

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado áreas de conocimiento'
        return context