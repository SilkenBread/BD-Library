from django.urls import path
from app.views.views_area_conocimiento import *
from app.views.dashboard_views import DashboardView

app_name= 'app'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('area_conocimiento/list/', AreaConocimientoListView.as_view(), name="area_conocimiento_list"),
    path('area_conocimiento/add/', AreaConocimientoCreateView.as_view(), name="area_conocimiento_create"),
    path('area_conocimiento/update/<str:pk>/', AreaConocimientoUpdateView.as_view(), name="area_conocimiento_update"),
    path('area_conocimiento/delete/<str:pk>/', AreaConocimientoDeleteView.as_view(), name="area_conocimiento_delete"),
]