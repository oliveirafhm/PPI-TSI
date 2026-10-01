from django.shortcuts import render
from django.urls import reverse_lazy
from helloworld.models import Funcionario
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from website.forms import InsereFuncionarioForm

def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
    ]
    # Dica: Ao invés de listar todos os campos em fields em formato de lista de strings, podemos utilizar fields = '__all__'. Dessa forma, o Django irá buscar todos os campos para você!

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")
    # O método reverse_lazy() serve para fazer a conversão de rotas (similar ao reverse()) mas em um momento em que o URLConf ainda não foi carregado pelo Django (que é o caso aqui).

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")