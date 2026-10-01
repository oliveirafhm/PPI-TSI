from django import forms
from helloworld.models import Funcionario

# Opção 1
# class InsereFuncionarioForm(forms.Form):

#     nome = forms.CharField(
#         label='Nome do Funcionário',
#         max_length=100
#     )

#     sobrenome = forms.CharField(
#         required=True,
#         max_length=255
#     )

#     cpf = forms.CharField(
#         required=True,
#         max_length=14
#     )

#     tempo_de_servico = forms.IntegerField(
#         required=True
#     )

#     remuneracao = forms.DecimalField()

# Opção 2
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