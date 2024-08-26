# Primeiro código em python com entrada de dados do teclado e com condição if, elif e else.

nome = input('Digite o seu nome: ')
peso = float(input('Digite agora o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc >= 28.00:
    print(f'Você está acima do peso. Seu Imc é de: {imc:.2f}')

elif imc < 28.00 and imc >= 22.00:
    print(f'Você está no peso recomendado. Seu Imc é de: {imc:.2f}')

else:
    print(f'Você está muito abaixo do peso ideal. Seu Imc é de: {imc:.2f}')
