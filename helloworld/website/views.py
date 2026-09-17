from django.shortcuts import render
from helloworld.models import Funcionario
from django.views.generic import ListView

def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"