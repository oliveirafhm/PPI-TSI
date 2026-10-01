from django import forms
from helloworld.models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario
        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
        ]
        # Campos que não estarão no form
        exclude = [
            'tempo_de_servico'
        ]
