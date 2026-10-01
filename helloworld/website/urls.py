from django.urls import path
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),

    path('funcionarios/', 
         views.FuncionarioListView.as_view(),
         name='lista_funcionarios'),

    # Utilizando o {id} para buscar o objeto
    path(
        'funcionario/<id>',
        views.FuncionarioUpdateView.as_view(),
        name='atualiza_funcionario'),

    # Utilizando o {slug} para buscar o objeto
    # path(
    #     'funcionario/<slug>',
    #     views.FuncionarioUpdateView.as_view(),
    #     name='atualiza_funcionario'),

    path(
        'funcionario/excluir/<pk>',
        views.FuncionarioDeleteView.as_view(),
        name='deleta_funcionario'),

    path(
        'funcionario/cadastrar/',
        views.FuncionarioCreateView.as_view(),
        name='cadastra_funcionario'),
]
