from rest_framework import viewsets, permissions
from api.models import FundoImobiliario
from api.serializers import FundoImobiliarioSerializer


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet que fornece automaticamente as ações padrão de um CRUD completo
    (Create, Read, Update, Delete) para o modelo FundoImobiliario.

    Equivale ao "sanduíche pronto do McDonald's": com pouquíssimas linhas,
    o DRF monta e disponibiliza todos os endpoints necessários.
    """

    # 1. Consulta ao Banco (Queryset):
    # Define quais registros do banco serão expostos por este ViewSet.
    # .all() traz todos os fundos imobiliários cadastrados.
    queryset = FundoImobiliario.objects.all()

    # 2. Transformador de Dados (Serializer):
    # Indica qual serializer será usado para validar e converter os dados (JSON <-> Model).
    serializer_class = FundoImobiliarioSerializer

    # 3. Controle de Acesso (Permissions):
    # Restringe o acesso aos endpoints. Neste caso, apenas usuários autenticados
    # (logados) podem visualizar, criar, editar ou excluir os dados.
    permission_classes = [permissions.IsAuthenticated]