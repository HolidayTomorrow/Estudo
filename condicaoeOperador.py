# Primeiro código em python com entrada de dados do teclado,com condição e operadores lógicos.
#Treinamento de condições com exercícios pessoais próprios.

nome = input('Digite o seu nome: ')
cpf = input('Digite o seu CPF: ')
idade = int(input('Digite a sua idade: '))

if not cpf == '05150360139' and not idade < 18:
    print(f'CPF não autorizado. Procure o administrador: {nome}')

elif cpf == '05150360139' and idade >= 18:
    print('CPF autorizado.')

else:
    print('Desculpe, algo deu errado.')
