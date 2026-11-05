# fundsfinder — API REST com Django REST Framework

Projeto desenvolvido durante a componente curricular **Programação para Internet**, do Curso Superior de Tecnologia em Sistemas de Informação (TSI) do Instituto Federal de Brasília (Campus Brasília).

O projeto consiste em uma API Web RESTful para cadastro, consulta, filtragem e gerenciamento de indicadores financeiros de **Fundos de Investimento Imobiliário (FIIs)**, desenvolvida de forma progressiva utilizando Python, Django e Django REST Framework (DRF).

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
- Postman (testes e validação de requisições)

## Estrutura do projeto

A organização dos diretórios e arquivos do projeto segue a seguinte estrutura:

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

O desenvolvimento com o Django REST Framework baseia-se no fluxo de quatro etapas principais:

1. **Model (`api/models.py`)**: Definição da entidade `FundoImobiliario`, armazenando ticker (`codigo`), setor de atuação, dividend yield médio, vacâncias e quantidade de ativos com identificador único universal (UUID v4).
2. **Serializer (`api/serializers.py`)**: Mapeamento bidirecional via `ModelSerializer`, convertendo instâncias do Django ORM em tipos primitivos do Python (para envio em JSON) e validando os dados recebidos para gravação.
3. **Views / ViewSets (`api/views.py`)**: Implementação da lógica de negócio e resposta a operações REST (através de `APIView` ou `ModelViewSet`).
4. **Routers e URLs (`api/urls.py` e `fundsfinder/urls.py`)**: Mapeamento e geração automática de rotas sob o prefixo padronizado `/api/v1/`.

## Ambiente virtual e dependências

Recomenda-se a utilização de um ambiente virtual para isolar as dependências do projeto.

### 1. Criar e ativar o ambiente virtual (Windows)

```cmd
py -m venv .venv
```

Ative o ambiente virtual:

```cmd
.venv\Scripts\activate
```

*(O terminal exibirá a indicação `(.venv)` no início da linha de comando confirmando a ativação).*

### 2. Instalação dos pacotes necessários

Com o ambiente virtual ativado, instale as dependências:

```cmd
pip install django djangorestframework django-filter
```

Caso esteja clonando o repositório em uma nova máquina:

```cmd
pip install -r requirements.txt
```

Para salvar e congelar as versões instaladas no arquivo de dependências:

```cmd
pip freeze > requirements.txt
```

## Banco de dados e migrações

Após a definição do modelo `FundoImobiliario`, gere e aplique as migrações para criar as tabelas no SQLite:

```cmd
python manage.py makemigrations api
python manage.py migrate
```

Crie um superusuário para gerenciar a aplicação e testar acessos autenticados na API:

```cmd
python manage.py createsuperuser
```

## Executando o projeto

Inicie o servidor local de desenvolvimento:

```cmd
python manage.py runserver
```

Acesse os serviços pelo navegador:

* **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **Interface Navegável da API (DRF Browsable API):** [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
* **Endpoint de Fundos:** [http://localhost:8000/api/v1/fundos](http://localhost:8000/api/v1/fundos)

## Endpoints da API

| Método HTTP | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/v1/fundos` | Lista todos os fundos cadastrados |
| `POST` | `/api/v1/fundos` | Cria um novo registro de fundo imobiliário |
| `GET` | `/api/v1/fundos/{id}` | Recupera os detalhes de um fundo pelo UUID |
| `PUT` | `/api/v1/fundos/{id}` | Atualização integral de um fundo pelo UUID |
| `PATCH` | `/api/v1/fundos/{id}` | Atualização parcial de um fundo pelo UUID |
| `DELETE` | `/api/v1/fundos/{id}` | Remove um fundo do banco de dados pelo UUID |

### Exemplo de Payload para Criação / Edição (POST / PUT)

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

## Filtros, Busca Textual e Paginação

* **Filtro por atributo:** `/api/v1/fundos?setor=logistica`
* **Busca textual:** `/api/v1/fundos?search=XPLG11`
* **Ordenação de resultados:** `/api/v1/fundos?ordering=-dividend_yield_medio_12m`
* **Paginação:** Resultados estruturados por padrão com metadados de paginação (`count`, `next`, `previous`, `results`).

## Controle de versão com Git

### Inicialização e envio da branch dedicada

Para versionar este projeto em uma branch independente dentro do repositório da disciplina:

```cmd
git init
git checkout -b api-fundsfinder
git add .
git commit -m "feat: commit inicial do projeto da API fundsfinder"
git remote add origin [https://github.com/oliveirafhm/PPI-TSI.git](https://github.com/oliveirafhm/PPI-TSI.git)
git push -u origin api-fundsfinder
```

### Arquivos ignorados (`.gitignore`)

O arquivo `.gitignore` impede o versionamento de dados sensíveis, arquivos temporários de compilação e do ambiente virtual:

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