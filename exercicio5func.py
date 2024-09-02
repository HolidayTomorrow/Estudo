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
    entrada = int(input('Insira '))
    if entrada != 0:
        valores.append(entrada)
    elif entrada == None or entrada == '' or entrada == 0 or entrada == '\n':
        flag = False
resultado = mult(*valores)
print(resultado)