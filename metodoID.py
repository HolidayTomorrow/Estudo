# Primeiro código em python reforçando os conceitos de código limpo, melhora de leitura e aprendendo o método ID.

IDADE = 18
ALTURA = 1.50

# Permissão de entrada para montanha russa


nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite a sua altura: '))

verificacao = input('Saiba que basta digitar (s/n) para confirmar se deseja visualizar a chave de confiança para verificação. Deseja chave? ')
if verificacao == 's' or verificacao == 'S':
    chave = (id(idade))
    print(f'A chave de confiança é {chave}')
    print('Verificando...')
    if idade < IDADE and altura < ALTURA:
        print(f'Você não pode acessar esse brinquedo, sua idade é de {idade} anos e sua altura é de {altura:.2f}m.')

    elif idade >= IDADE and altura >= ALTURA:
        print(f'Você pode acessar o brinquedo. Diverta-se, {nome}.')

    elif idade >= IDADE and altura < ALTURA:
        print(f'Você não tem a altura necessária para acessar esse brinquedo. Sua altura é de {altura:.2f}m.')

    else:
        print(f'Você não tem idade suficiente para acessar esse brinquedo. Sua idade é de {idade} anos.')
    print(f'A chave de confiança é {chave}')
else:
    if idade < IDADE and altura < ALTURA:
        print(f'Você não pode acessar esse brinquedo, sua idade é de {idade} anos e sua altura é de {altura:.2f}m.')

    elif idade >= IDADE and altura >= ALTURA:
        print(f'Você pode acessar o brinquedo. Diverta-se, {nome}.')

    elif idade >= IDADE and altura < ALTURA:
        print(f'Você não tem a altura necessária para acessar esse brinquedo. Sua altura é de {altura:.2f}m.')

    else:
        print(f'Você não tem idade suficiente para acessar esse brinquedo. Sua idade é de {idade} anos.')



    
