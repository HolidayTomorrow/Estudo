# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import os
import sys
import json
import types
from itertools import groupby
from itertools import count
import functools

CAMINHO_ARQUIVO_APROVADOS = 'lista_de_alunos_aprovados.json'
CAMINHO_ARQUIVO_REPROVADOS = 'lista_de_alunos_reprovados.json'
class Avaliacao():
    def __init__(self, args):
        self.alunos = list(args)
        
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def passaram(args):
    alunos = list(args)
    aprovados = [
        {**aluno}
        for aluno in alunos
        if aluno['nota'] in ['A', 'B']
    ]
    salvar(aprovados, CAMINHO_ARQUIVO_APROVADOS)
    for aluno in aprovados:
        print(aluno)
    def retornar_aprovados():
        return aprovados
    return retornar_aprovados


def nao_passaram(args):
    alunos = list(args)
    reprovados = [
        {**aluno}
        for aluno in alunos
        if aluno['nota'] in ['C', 'D']
        ]
    
    for aluno in reprovados:
        print(aluno)
    def retornar_reprovados():
        return reprovados
    return retornar_reprovados

def ordena(alunos):
    return alunos['nota']

def salvar(lista, caminho_arquivo):
    dados = lista
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False)
        return dados

def ler(lista, caminho_arquivo):
    dados = []
    try: 
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(lista, caminho_arquivo)
        return dados

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

# for chave, grupo in grupos:
#     lista_aluno.extend(iter(grupo))

avaliacao = Avaliacao(alunos)
aprovados = passaram(avaliacao.alunos)()
reprovados = nao_passaram(avaliacao.alunos)()

salvar(aprovados, CAMINHO_ARQUIVO_APROVADOS)
salvar(reprovados, CAMINHO_ARQUIVO_REPROVADOS)


