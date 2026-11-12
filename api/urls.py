from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewSet

# Define o namespace da aplicação para organização e reversão de URLs (ex.: 'api:fundoimobiliario-list')
app_name = 'api'

# Instancia o roteador padrão do DRF, que gera automaticamente todas as rotas REST (GET, POST, PUT, PATCH, DELETE)
# trailing_slash=False torna opcional/remove a barra final obrigatória nas URLs (ex.: /api/v1/fundos em vez de /api/v1/fundos/)
router = DefaultRouter(trailing_slash=False)

# Registra o ViewSet no roteador associando-o ao prefixo de rota 'fundos'
# O r'' (raw string) evita que barras invertidas sejam interpretadas como caracteres de escape
router.register(r'fundos', FundoImobiliarioViewSet)

# Expõe a lista de padrões de URL gerados automaticamente pelo roteador para o Django
urlpatterns = router.urls