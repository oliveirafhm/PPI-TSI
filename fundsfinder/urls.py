"""
URL configuration for fundsfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Lista global de rotas (URLs) do projeto fundsfinder
urlpatterns = [
    # Rota base versionada da API (v1):
    # Delega todas as requisições iniciadas com 'api/v1/' para o arquivo api/urls.py.
    # O parâmetro namespace='api' vincula-se ao app_name definido no aplicativo.
    path('api/v1/', include('api.urls', namespace='api')),

    # Rotas de autenticação nativa do Django REST Framework:
    # Habilita os endpoints de login e logout na interface navegável (Browsable API),
    # essenciais para testar views protegidas por permission_classes diretamente no navegador.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Rota padrão do painel administrativo do Django
    path('admin/', admin.site.urls),
]