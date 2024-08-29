"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.

"""
import os
palavra_secreta = input('Qual será a palavra secreta? ')
letras_acertadas = ''
numero_de_tentativas = 0
i = 0
flag = False
condicao = True
print('Adivinhe as letras que formam a palavra secreta e ganhe o jogo.')
print('')

while condicao:
    if flag == True:
        print('Adivinhe as letras que formam a palavra secreta e ganhe o jogo.')
        print('')
        palavra_secreta = input('Qual será a palavra secreta? ')
    letra_digitada = input('Qual a letra correta? ')
    numero_de_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra de cada vez.')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        i += 1
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        if palavra_formada == len(palavra_secreta):
            print(f'Você errou. Acertos até agora {i}: {palavra_formada}')
    print(f'Você acertou. Acertos até agora {i}: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra secreta era', palavra_secreta)
        print('Tentativas:', numero_de_tentativas)
        print('')
        reiniciar = input('Deseja jogar outra vez? (s/n) ')
        print('')
        flag = False
        if reiniciar == 's' or reiniciar == 'S':
            letras_acertadas = ''
            numero_de_tentativas = 0
            i = 0
            flag = True
        else:
            print("FIM DE JOGO.")
            condicao = False