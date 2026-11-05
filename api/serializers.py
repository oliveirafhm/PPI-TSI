from rest_framework import serializers
from api.models import FundoImobiliario

class FundoImobiliarioSerializer(serializers.ModelSerializer):
    """
    Serializer responsável por converter instâncias do modelo FundoImobiliario
    em representações nativas do Python (para envio em JSON/XML) e vice-versa,
    além de validar os dados recebidos nas requisições da API.
    """
    class Meta:
        # Define qual modelo do Django ORM este serializer utilizará como base
        model = FundoImobiliario

        # Lista explícita dos campos que serão expostos/serializados pela API
        # (Boa prática: evita expor atributos indesejados caso novos campos surjam no Model)
        fields = [
            'id',
            'codigo',
            'setor',
            'dividend_yield_medio_12m',
            'vacancia_financeira',
            'vacancia_fisica',
            'quantidade_ativos',
        ]