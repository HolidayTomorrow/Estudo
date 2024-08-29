"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os
condicao = True
contador = 0
while condicao:
    print("Selecione uma opção")
    escolha = input('[i]nserir [a]pagar [l]istar: ')
    if escolha =='l' and contador == 0:
        print('Não há dados para listar.')
        break
    elif escolha =='a' and contador == 0:
        print('Não há dados para apagar.')