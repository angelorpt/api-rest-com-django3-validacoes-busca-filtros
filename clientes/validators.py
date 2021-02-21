import re

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_rg):
    return len(numero_rg) == 9

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
