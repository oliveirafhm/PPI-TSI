from django.urls import path
# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
    path('funcionarios/', 
         views.ListaFuncionarios.as_view(),
         name='funcionarios'),
]
