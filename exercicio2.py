"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista_a = ['Maria', 'Helena', 'Luiz']

indices = range(len(lista_a))

for indice in indices:
    print(indice, lista_a[indice], type(lista_a[indice]))
