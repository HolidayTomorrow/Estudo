# Primeiro programa em python utilizando laço de repetição.


text = input('Insira uma frase ou um texto: ')
validation = input('Deseja iniciar a contagem de caracteres? (s/n) ')
i = 0
space = input('Deseja contabilizar os espaços entre as palavras? (s/n)')
print('')
if validation == 's' or validation =='S':
    while i < len(text):
        character = text[i]

        if character == ' ' and (space == 'n' or space == 'N'):
            print(character)
            i += 1
        elif character == ' ' and (space == 's' or space == 'S'):
            print(character, text.count(character))
            i += 1
        else:
            print(character, text.count(character))
            i += 1
elif validation == 'n' or validation == 'N':
    print('Não foi realizado a contagem dos caracteres.')