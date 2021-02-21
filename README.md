# API REST com Django3: Validações, buscas, filtros

## Detalhes

Projeto baseado em um curso da Alura de Django3

[API com Django 3: Validações, buscas, filtros e deploy](https://cursos.alura.com.br/course/api-django-3-validacoes-buscas-filtros-deploy)

* Descrição
    * Aprenda como validar os campos de sua API, utilizando Django Rest Framework
    * Saiba como incluir filtros, buscas e ordenação em seus endpoints
    * Crie uma boa arquitetura em seus projetos Django Rest API
    * Coloque sua API no ar realizando o deploy
    * Descubra como criar suas próprias APIs com Django

## Anotações Pessoais do Curso

### Ambiente de Desenvolvimento

**Preparando o Ambiente**

```bash
$ python -m venv ./venv
```

**Ativando o ambiente no Windows**

[documentação venv](https://docs.python.org/pt-br/3/library/venv.html)

```bash
$ venv\Scripts\activate
```

**Instalando o Django no ambiente ativado**
```bash
$ pip install -r requirements.txt
```

**Criando projeto utilizando Django Admin**
```bash
$ django-admin startproject setup .
```
**No arquivo "settings.py" alterar:**
* LANGUAGE_CODE = 'pt-br'
* TIME_ZONE = 'America/Sao_Paulo'

**Rodando o serviço**
```bash
$ python manage.py runserver
```
