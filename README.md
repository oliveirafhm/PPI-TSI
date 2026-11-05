# fundsfinder — API REST com Django REST Framework

Projeto desenvolvido durante a componente curricular **Programação para Internet**, do Curso Superior de Tecnologia em Sistemas de Informação (TSI) do Instituto Federal de Brasília (Campus Brasília).

O projeto consiste numa API Web RESTful para registo, consulta, filtragem e gestão de indicadores financeiros de **Fundos de Investimento Imobiliário (FIIs)**, desenvolvida de forma progressiva com recurso ao Django e ao Django REST Framework (DRF).

## Professor

**Prof. Fábio Henrique Monteiro Oliveira**  
E-mail: `fabio.oliveira@ifb.edu.br`

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework (DRF)
- django-filter
- SQLite
- Git e GitHub
- Postman (testes e validação de endpoints)

## Estrutura do projeto

A organização das pastas e ficheiros do projeto segue a seguinte disposição:

```text
fundsfinder/
├── manage.py
├── requirements.txt
├── .gitignore
├── db.sqlite3
│
├── fundsfinder/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── api/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Arquitetura e camadas da API

O desenvolvimento com o Django REST Framework assenta no fluxo de quatro camadas principais:

1. **Model (`api/models.py`)**: Definição da entidade `FundoImobiliario`, armazenando código de negociação (`codigo`), setor de atuação, dividend yield médio, vacâncias e quantidade de imóveis, com chave primária em formato UUID.
2. **Serializer (`api/serializers.py`)**: Mapeamento bidirecional via `ModelSerializer`, convertendo instâncias do Django ORM em dados estruturados (JSON) e executando a validação dos dados recebidos nas requisições.
3. **Views / ViewSets (`api/views.py`)**: Implementação da lógica de negócio e resposta a operações REST (através de `APIView` ou `ModelViewSet`).
4. **Routers e URLs (`api/urls.py` e `fundsfinder/urls.py`)**: Configuração de rotas automatizadas e versionamento dos serviços sob o prefixo `/api/v1/`.

## Configuração do ambiente virtual

Recomenda-se a utilização de um ambiente virtual para isolamento das dependências da aplicação.

### 1. Criar e ativar o ambiente virtual (Windows)

```cmd
py -m venv .venv
```

Ative o ambiente virtual:

```cmd
.venv\Scripts\activate
```

*(O terminal exibirá a indicação `(.venv)` no início da linha de comandos).*

### 2. Instalação de dependências

Com o ambiente ativado, instale os módulos necessários:

```cmd
pip install django djangorestframework django-filter
```

Caso esteja a configurar o projeto a partir do repositório:

```cmd
pip install -r requirements.txt
```

Para atualizar o ficheiro de dependências:

```cmd
pip freeze > requirements.txt
```

## Base de dados e migrações

Após configurar o modelo `FundoImobiliario`, gere e aplique as migrações:

```cmd
python manage.py makemigrations api
python manage.py migrate
```

Crie o utilizador administrador para acesso ao painel e à API autenticada:

```cmd
python manage.py createsuperuser
```

## Execução da aplicação

Inicie o servidor de desenvolvimento local:

```cmd
python manage.py runserver
```

Aceda aos serviços através do navegador:

* **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **Interface Navegável da API (DRF Browsable API):** [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
* **Lista de Fundos:** [http://localhost:8000/api/v1/fundos](http://localhost:8000/api/v1/fundos)

## Endpoints da API

| Método HTTP | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/v1/fundos` | Listagem de todos os fundos registados |
| `POST` | `/api/v1/fundos` | Criação de um novo fundo imobiliário |
| `GET` | `/api/v1/fundos/{id}` | Obtenção dos dados de um fundo por UUID |
| `PUT` | `/api/v1/fundos/{id}` | Atualização integral de um fundo por UUID |
| `PATCH` | `/api/v1/fundos/{id}` | Atualização parcial de um fundo por UUID |
| `DELETE` | `/api/v1/fundos/{id}` | Remoção de um fundo da base de dados |

### Exemplo de Payload para Envio (POST / PUT)

```json
{
  "codigo": "XPLG11",
  "setor": "logistica",
  "dividend_yield_medio_12m": 6.30,
  "vacancia_financeira": 7.87,
  "vacancia_fisica": 12.36,
  "quantidade_ativos": 19
}
```

## Recursos de consulta: filtros, busca e paginação

* **Filtro por setor:** `/api/v1/fundos?setor=logistica`
* **Busca textual:** `/api/v1/fundos?search=XPLG11`
* **Ordenação de dados:** `/api/v1/fundos?ordering=-dividend_yield_medio_12m`
* **Paginação:** Resultados estruturados por padrão com metadados (`count`, `next`, `previous`, `results`).

## Controlo de versões (Git)

As etapas de implementação devem ser devidamente comitadas no repositório:

```cmd
git status
git add .
git commit -m "feat: implementa camada de serialização e views da API"
git push
```

### Ficheiros ignorados (`.gitignore`)

Certifique-se de que o ficheiro `.gitignore` impede a submissão de dependências locais e artefactos de compilação:

```text
.venv/
__pycache__/
*.py[cod]
db.sqlite3
.vscode/
```

## Material de apoio

* **PYTHON ACADEMY.** *Desenvolvimento de APIs com Django REST Framework*. [S. l.]: Python Academy, [s.d.]. E-book. Disponível em: [https://pythonacademy.com.br/](https://pythonacademy.com.br/). Acesso em: 30 jul. 2026.
* Documentação oficial do Django REST Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

## Componente curricular

**Programação para Internet**  
Curso Superior de Tecnologia em Sistemas de Informação (TSI)  
Instituto Federal de Educação, Ciência e Tecnologia de Brasília (IFB) — Campus Brasília