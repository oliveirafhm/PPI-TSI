import uuid
from django.db import models


class FundoImobiliario(models.Model):
    """
    Representa a entidade de um Fundo de Investimento Imobiliário (FII) na base de dados.
    Herda de models.Model para usufruir de todos os recursos do ORM do Django.
    """

    # Lista de tuplas (chave_banco, rotulo_exibicao) para restringir as opções de setor
    SETOR_CHOICES = [
        ('hospital', 'Hospital'),
        ('hotel', 'Hotel'),
        ('hibrido', 'Híbrido'),
        ('lajes_corporativas', 'Lajes Corporativas'),
        ('logistica', 'Logística'),
        ('outros', 'Outros'),
        ('residencial', 'Residencial'),
        ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.'),
    ]

    # Identificador único universal (UUID v4) usado como chave primária em vez de inteiros sequenciais
    # editable=False impede que o campo apareça em formulários ou no Django Admin para alteração manual
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Código/Ticker do fundo negociado em bolsa (ex.: HGLG11, XPLG11)
    codigo = models.CharField(
        max_length=8,
        null=False,  # Não permite valor nulo na coluna da base de dados
        blank=False,  # Torna o preenchimento obrigatório em formulários e APIs
    )

    # Setor de atuação do fundo imobiliário com opções pré-definidas via SETOR_CHOICES
    setor = models.CharField(
        max_length=30,
        choices=SETOR_CHOICES,
        null=False,
        blank=False,
    )

    # Dividend Yield médio acumulado nos últimos 12 meses (%)
    # max_digits=5 e decimal_places=2 permitem valores até 999.99 (ex.: 12.35)
    dividend_yield_medio_12m = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    # Percentual de receita financeira não recebida por falta de locação (%)
    vacancia_financeira = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    # Percentual de área física total desocupada/sem locatários (%)
    vacancia_fisica = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    # Quantidade total de imóveis ou ativos sob gestão do fundo
    quantidade_ativos = models.IntegerField(
        default=0,  # Inicia com 0 se nenhum valor for informado
        null=False,
        blank=False,
    )

    def __str__(self):
        """
        Retorna a representação textual do objeto ao ser impresso ou listado no Django Admin.
        get_setor_display() retorna o rótulo legível da tupla (ex.: 'Logística') em vez da chave ('logistica').
        """
        return f"{self.codigo} - {self.get_setor_display()}"