from django.urls import path
from app.views.views_area_conocimiento import *

app_name= 'app'

urlpatterns = [
    path('area_conocimiento/list/', AreaConocimientoListView.as_view(), name="area_conocimiento_list"),
]