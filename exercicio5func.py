# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
        args = list(args)
        multiplica = 1
        for arg in args:
            multiplica *= arg
        return multiplica
entrada = []
valores = []
contador = 0
flag = True
while flag:
    entrada = input('Insira ')
    for valor in entrada:
        if valor != '0':
            valores += valor
        elif valor == None or valor == '' or valor == '0' or valor == '\n':
            flag = False
resultado = mult(valores)
print(resultado)