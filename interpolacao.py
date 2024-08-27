# Primeiro exercício de interpolação de variáveis.
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal



nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
diasTrabalhados = int(input('Digite os dias trabalhados: '))



print('Seu nome é %s e sua idade é %d' %(nome, idade))
print('Seu salário é R$%.2f' %(salario))
print('Dias trabalhados em hexadecimal é %08X' %(diasTrabalhados))
