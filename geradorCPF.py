"""
Gerador de CPF com a biblioteca random, gerando número automáticos
mas que, por meio dos cálculos utilizando o algoritmo de CPF, se torna
um CPF válido
"""

import os
import re
import random
condicao = int(input('Quantos CPF\' deseja gerar? '))
contador = 0
while contador < condicao:
    cpf_digitado = ''
    for _ in range(9):
        cpf_digitado += str(random.randint(0, 9))
    multiplicadores_primeiro_digito = 10
    multiplicadores_segundo_digito = 11
    cpf_coletado = re.sub(r'[^0-9]', '', cpf_digitado)
    
    resultado = 0 
    for digito_cpf in cpf_coletado:
        resultado += int(digito_cpf)*multiplicadores_primeiro_digito
        multiplicadores_primeiro_digito -= 1
    resultado = ((resultado*10) % 11) if ((resultado*10) % 11) <= 9 else 0
    cpf_coletado += str(resultado)
    resultado = 0
    for digito_cpf in cpf_coletado:
        resultado += int(digito_cpf) * multiplicadores_segundo_digito
        multiplicadores_segundo_digito -= 1
    resultado = ((resultado*10) % 11) if ((resultado*10) % 11) <= 9 else 0
    cpf_coletado += str(resultado)
    contador += 1
    print(cpf_coletado)