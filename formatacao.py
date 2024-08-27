#Primeiro exercício de formatação de strings.
# s - string
# d e i - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(<>^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
diasTrabalhados = int(input('Digite os dias trabalhados: '))



print(f'Seu nome é {nome}')
print(f'Sua idade é {idade: >100}')
print(f'Seu salário é R${salario:0<+9,.2f}')# O sinal "<" joga o sinal "+" 9 casas à esquerda.
print(f'Os dias trabalhados em hexadecimal é: {diasTrabalhados:08X}')
print(f'{idade!r}')
