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

## Validações

[DOC - Validações Django REST Framework](https://www.django-rest-framework.org/api-guide/validators/)

**Visualizando a instância do Serializer e as validações importadas do Model**
```bash
$ python manage.py shell

>>>from clientes.serializers import ClienteSerializer
>>>s = ClienteSerializer()
>>>print(repr(s))

ClienteSerializer():
    id = IntegerField(label='ID', read_only=True)
    nome = CharField(max_length=100)
    email = EmailField(max_length=30)
    cpf = CharField(max_length=11, validators=[<UniqueValidator(queryset=Cliente.objects.all())>])
    rg = CharField(max_length=9)
    celular = CharField(max_length=14)
    ativo = BooleanField()
```

**Validando a quantidade de dígitos do CPF "serializers.py"**
```python
class ClienteSerializer(serializers.ModelSerializer):
    ...
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve possuir 11 dígitos")
```

**Separando a responsabilidade da validação em outro arquivo**

* validators.py

```python
def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_rg):
    return len(numero_rg) == 9

def celular_valido(numero_celular):
    return len(celular) > 11
```

* serializers.py

```python
...
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    ...
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve ter 11 dígitos"})

        if not nome_valido(data['nome'])
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve possuir 9 dígitos"})

        if not celular_valido(data['celular'])
            raise serializers.ValidationError({'celular': "O celular deve possuir 11 dígitos"})
        
        return data
```

**Instalando a biblioteca de validação de documentos**

[DOC - Validate DOC_BR](https://pypi.org/project/validate-docbr/)

```bash
$ pip install validate-docbr
```

* No arquivo "validator.py"

```python
...
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)
```

## Populando o Banco com Dados Fictícios

[DOC - Faker](https://faker.readthedocs.io/en/master/)

**Instalando a biblioteca faker**

```bash
$ pip install Faker
```

**Criar um arquivo na raiz do projeto: "populate_script.py"**

```python
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clientes.models import Cliente

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
        p.save()

criando_pessoas(50)
```

**Executando o script**
```bash
$ python populate_script.py
```

## Paginação da API

[DOC - Paginação](https://www.django-rest-framework.org/api-guide/pagination/)

**Alterando a paginação no arquivo "settings.py"**
```python
...
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## Ordenando

### Admin

**Alterando a ordenação no Admin: "admin.py"**
```python
...
class Clientes(admin.ModelAdmin):
    ...
    ordering = ('nome',)
```

### API

[DOC - Filtering](https://www.django-rest-framework.org/api-guide/filtering/)

1. Alterando a ordenação na API
```bash
$ pip install django-filter
```

2. No arquivo "settings.py" adicionar o app
```python
INSTALLED_APPS = [
    ...
    'django_filters',
]
```

3. No arquivo "views.py"

```python
from rest_framework import ..., filters
...
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']

```