nome = 'Marcelo dos Santos Rigobeli Rocha'
peso = 77.5
altura = 1.66
imc = peso / altura ** 2

string = 'nome = {n} peso = {p:.2f} altura = {a:.2f}'
formato = string.format(n = nome, p = peso, a = altura)

print(formato)