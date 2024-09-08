# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00,},
    {'nome': 'Produto 1', 'preco': 22.32,},
    {'nome': 'Produto 3', 'preco': 10.11,},
    {'nome': 'Produto 2', 'preco': 105.87,},
    {'nome': 'Produto 4', 'preco': 69.90,},
]
import copy
import sys
import os
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key = lambda produto: produto['nome'],
    reverse = False
    )

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key = lambda preco: preco['preco'],
    reverse = False
    )
print(*produtos, sep = '\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
