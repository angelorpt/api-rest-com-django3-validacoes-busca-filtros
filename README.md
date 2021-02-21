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