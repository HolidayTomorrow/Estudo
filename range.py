"""
Entendendo a função range

"""
palavra = ''
condicao = True

while condicao:
    palavra += input('Insira seu nome: ')
    resposta = input('Deseja inserir mais nomes? (s/n): ')
    if resposta == 'n' or resposta == 'N':
        condicao = False

indices = range(len(palavra))
print(indices)
for indice in indices:
    print(indice, palavra[indice])
palavra = ''

