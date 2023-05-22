from django.urls import path
from app.views import firstview

urlpatterns = [
    path('subtest/', firstview),
]