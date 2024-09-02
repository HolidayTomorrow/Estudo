# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def mult(*args):
    args = list(args)
    multiplica = 1
    for arg in args:
        multiplica *= arg
    return multiplica
def parimpar(args):
    args = float(args)
    numero = 'O número é par'if args % 2 == 0 else 'O número é ímpar'
    return numero
entrada = []
valores = []
flag = True
while flag:
    entrada = int(input('Insira '))
    if entrada != 0:
        valores.append(entrada)
    elif entrada == None or entrada == '' or entrada == 0 or entrada == '\n':
        flag = False
resultado = mult(*valores)
print(resultado)
numero = parimpar(resultado)
print(numero)