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

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
    },
]

condicao = True
while condicao:
    iniciar = input('Deseja responder as perguntas?(s/n) ')
    if iniciar == 'n' or iniciar == 'N':
        condicao = False
    else:
        for pergunta in perguntas:
            for valor in pergunta.values():
                print('Escolha a alternativa correta')
                
                print(valor)
