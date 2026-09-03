# PPI-TSI

Projeto desenvolvido durante a componente curricular **Programação para Internet**, do Curso Superior de Tecnologia em Sistemas para Internet (TSI).

O projeto será desenvolvido progressivamente ao longo do semestre, acompanhando os conteúdos e as atividades práticas trabalhados em aula.

## Professor

**Prof. Fábio Henrique Monteiro Oliveira**  
E-mail: `fabio.oliveira@ifb.edu.br`

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Git e GitHub

## Estrutura inicial do projeto

A estrutura inicial do projeto está organizada da seguinte forma:

```text
PPI-TSI/
└── helloworld/
    ├── manage.py
    │
    ├── helloworld/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   ├── wsgi.py
    │   └── models.py
    │
    └── website/
        ├── migrations/
        │   └── __init__.py
        │
        ├── static/
        │   └── website/
        │       ├── css/
        │       ├── img/
        │       └── js/
        │
        ├── templates/
        │   └── website/
        │       └── _layouts/
        │
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── tests.py
        ├── urls.py
        └── views.py
````

> A estrutura do projeto poderá ser modificada e ampliada ao longo das aulas.

## Organização do projeto

### Projeto `helloworld`

A pasta `helloworld` contém os principais arquivos de configuração e desenvolvimento do projeto Django.

* `manage.py` — utilitário de linha de comando para administração do projeto;
* `settings.py` — configurações do projeto;
* `urls.py` — definição das URLs principais do projeto;
* `models.py` — definição dos Models utilizados no projeto;
* `asgi.py` — ponto de entrada para servidores compatíveis com ASGI;
* `wsgi.py` — ponto de entrada para servidores compatíveis com WSGI.

### Aplicação `website`

A aplicação `website` concentra os recursos relacionados ao desenvolvimento da aplicação Web.

* `views.py` — implementação das Views;
* `urls.py` — definição das URLs específicas da aplicação;
* `admin.py` — configuração do Django Admin;
* `apps.py` — configuração da aplicação;
* `migrations/` — arquivos de migração relacionados ao banco de dados;
* `templates/` — templates da aplicação;
* `static/` — arquivos estáticos da aplicação.

### Templates

Os templates da aplicação estão organizados em:

```text
website/templates/website/_layouts/
```

A pasta `_layouts` é utilizada para organizar templates de estrutura que podem ser reutilizados por diferentes páginas da aplicação.

### Arquivos estáticos

Os arquivos estáticos da aplicação estão organizados em:

```text
website/static/website/
├── css/
├── img/
└── js/
```

As pastas são destinadas a:

* `css/` — arquivos de estilos CSS;
* `img/` — imagens utilizadas pela aplicação;
* `js/` — arquivos JavaScript.

### URLs

O projeto utiliza dois níveis de organização das URLs.

As URLs principais do projeto estão definidas em:

```text
helloworld/helloworld/urls.py
```

As URLs específicas da aplicação `website` estão definidas em:

```text
helloworld/website/urls.py
```

Essa organização permite separar as URLs gerais do projeto das URLs relacionadas às funcionalidades da aplicação.

## Ambiente virtual

Recomenda-se utilizar um ambiente virtual para isolar as dependências do projeto.

No Windows:

```cmd
py -m venv .venv
```

Ative o ambiente virtual:

```cmd
.venv\Scripts\activate
```

Quando o ambiente estiver ativo, o terminal deverá apresentar `(.venv)` no início da linha.

## Instalação do Django

Com o ambiente virtual ativado:

```cmd
python -m pip install django
```

Verifique a versão instalada:

```cmd
django-admin --version
```

## Executando o projeto

Entre na pasta que contém o arquivo `manage.py`:

```cmd
cd helloworld
```

Execute o servidor de desenvolvimento:

```cmd
python manage.py runserver
```

A aplicação poderá ser acessada pelo navegador em:

```text
http://localhost:8000
```

## Banco de dados

Durante o desenvolvimento, o projeto utiliza o SQLite.

Após alterações nos Models, crie as migrações:

```cmd
python manage.py makemigrations
```

Aplique as migrações:

```cmd
python manage.py migrate
```

As migrations devem ser mantidas no repositório Git, pois registram a evolução da estrutura do banco de dados.

O arquivo `db.sqlite3`, utilizado como banco de dados local durante o desenvolvimento, não deve ser enviado ao repositório.

## Django Admin

Para criar um usuário administrador:

```cmd
python manage.py createsuperuser
```

Depois de executar o servidor, acesse:

```text
http://localhost:8000/admin/
```

O Django Admin será utilizado durante as aulas para gerenciamento dos dados da aplicação.

## Git e GitHub

As alterações realizadas durante as aulas devem ser registradas no Git.

Verifique o estado do repositório:

```cmd
git status
```

Adicione as alterações:

```cmd
git add .
```

Crie um commit:

```cmd
git commit -m "Descrição da alteração"
```

Envie as alterações para o GitHub:

```cmd
git push
```

## Utilizando o projeto inicial

O projeto inicial disponibilizado pelo professor pode ser clonado com:

```cmd
git clone https://github.com/oliveirafhm/PPI-TSI.git
```

Entre na pasta criada:

```cmd
cd PPI-TSI
```

Após criar o seu próprio repositório no GitHub, altere o endereço do repositório remoto:

```cmd
git remote set-url origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

Verifique o endereço configurado:

```cmd
git remote -v
```

A partir desse momento, os comandos `git push` serão direcionados para o repositório do estudante.

## Arquivos que não devem ser enviados

O arquivo `.gitignore` deve impedir o envio de arquivos e pastas específicos do ambiente local:

```text
.venv/
__pycache__/
*.py[cod]
db.sqlite3
.env
.vscode/
```

## Material de apoio

A componente curricular utiliza como material de apoio o e-book:

**PYTHON ACADEMY.** *Desenvolvimento web com Python e Django*. [S. l.]: Python Academy, [s.d.]. E-book.

Disponível em: [https://pythonacademy.com.br/](https://pythonacademy.com.br/)

Acesso em: 30 jul. 2026.

O material será utilizado como referência para os conteúdos relacionados ao desenvolvimento de aplicações Web com Python e Django.

## Desenvolvimento

O projeto será desenvolvido de forma incremental durante o semestre, contemplando os conteúdos trabalhados na componente curricular, incluindo:

1. Introdução ao Django;
2. Estrutura de projetos e aplicações;
3. Models e ORM;
4. Migrações e banco de dados;
5. Django Admin;
6. Templates e Bootstrap;
7. Views e URLs;
8. Forms;
9. Autenticação e autorização;
10. Desenvolvimento de APIs REST;
11. Consumo de APIs;
12. Integração entre frontend e backend;
13. Boas práticas para projeto de APIs;
14. Deploy de aplicações Web.

## Componente curricular

**Programação para Internet**
Curso Superior de Tecnologia em Sistemas para Internet (TSI)

Este repositório é utilizado para acompanhamento e desenvolvimento das atividades práticas da componente curricular.
