# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    if args == tuple:
        args = list(args)
        multiplica = 1
        for arg in args:
            multiplica *= arg
        return multiplica
valores = []
contador = 0
flag = True
while flag:
    valores = input('Insira ')
    contador += 1
    for valor in valores:
        if valor == None or valor == '0' or valor == '' or valor == '\n':
            flag = False
resultado = mult(*valores)
print(resultado)