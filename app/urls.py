from django.urls import path
from app.views.area_conocimiento_views import *
from app.views.autores_views import *
from app.views.dashboard_views import DashboardView

app_name= 'app'

urlpatterns = [
    #Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Area Conocimiento
    path('area_conocimiento/list/', AreaConocimientoListView.as_view(), name="area_conocimiento_list"),
    path('area_conocimiento/add/', AreaConocimientoCreateView.as_view(), name="area_conocimiento_create"),
    path('area_conocimiento/update/<str:pk>/', AreaConocimientoUpdateView.as_view(), name="area_conocimiento_update"),
    path('area_conocimiento/delete/<str:pk>/', AreaConocimientoDeleteView.as_view(), name="area_conocimiento_delete"),
    #Autores
    path('autores/list/', AutoresListView.as_view(), name="autores_list"),
    path('autores/add/', AutoresCreateView.as_view(), name="autores_create"),
    path('autores/update/<str:pk>/', AutoresUpdateView.as_view(), name="autores_update"),
    path('autores/delete/<str:pk>/', AutoresDeleteView.as_view(), name="autores_delete"),
    #Libros
]