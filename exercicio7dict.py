# Exercício - sistema de perguntas e respostas
# Preciso de variáveis que recebam o número da opção digitada.

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

condicao = True
while condicao:
    iniciar = input('Deseja responder as perguntas?(s/n) ')
    os.system('cls')
    if iniciar == 'n' or iniciar == 'N':
        condicao = False
        os.system('cls')
        print('Fim.')
    else:
        acertos = 0
        for pergunta in perguntas:
            print('\nEscolha a alternativa correta\n')

            print('Pergunta: ', pergunta['Pergunta'])

            opcoes = pergunta['Opções']
            for i, opcao in enumerate(opcoes):
                print(f'{i})', opcao)

            escolha = input('Escoha uma opção: ')

            acertou = False
            qtd_opcoes = len(opcoes)

            if escolha.isdigit():
                escolha = int(escolha)

            if escolha is not None:
                if escolha >= 0 and escolha < qtd_opcoes:
                    if opcoes[escolha] == pergunta['Resposta']:
                        acertou = True
            
            print()
            if acertou:
                acertos += 1
                print('Acertou 👍')
            else:
                print('Errou ❌')

            print()
        print('Você acertou', acertos)
        print('de', len(perguntas), 'perguntas.')
