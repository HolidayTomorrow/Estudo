"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os
condicao = True
lista = []
while condicao:
    print("Selecione uma opção")
    escolha = input('[i]nserir [a]pagar [l]istar [s]air: ')
    if escolha =='i':
        os.system('cls')
        valor = input('Insira o nome do produto: ')
        lista.append(valor) # O cabeçudo estava realizando uma atribuição além do método do objeto string.
    elif escolha =='a':
        os.system('cls')
        indiceEscolhido = input('Escolha um índice válido para apagar: ')
        try:
            indice = int(indiceEscolhido)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('Índice não existente na lista.')
        except Exception:
            print('Erro desconhecido')
    elif escolha =='l':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif escolha == 's':
        os.system('cls')
        print('Saindo...')
        condicao = False
    else:
        print('Por favor, escolha i, a, l ou s para sair.')
    
