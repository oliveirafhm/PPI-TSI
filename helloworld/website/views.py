from django.shortcuts import render
from helloworld.models import Funcionario


def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)