
from . import views
from django.urls import path

urlpatterns = [
    path('', views.muestra_datos, name='prueba1'),
]
