# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p][::]
# Obs.: a função len retorna a quantidade de caracteres.


nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#salario = float(input("Digite seu salário: "))
#diasTrabalhados = int(input('Digite os dias trabalhados: '))



print(f'Seu nome tem {len(nome)} caracteres')
print(f'Ele fica engraçado de trás para frente, veja: {nome[::-1]}')