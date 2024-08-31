"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.:    746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0
    
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
    contrário disso:
"""
import os
import re
condicao = True
while condicao:
    multiplicadores_primeiro_digito = 10
    multiplicadores_segundo_digito = 11
    # cpf_digitado = '74682489070' 
    cpf_digitado = input('CPF: ')
    cpf_digitado = re.sub(r'[^0-9]', '', cpf_digitado)
    cpf_coletado = cpf_digitado[:9]
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
    if cpf_coletado == cpf_digitado:
        os.system('cls')
        print('CPF Válido!')
    elif cpf_coletado != cpf_digitado:
        os.system('cls')
        print('CPF Inválido!')
    continuar = input('Deseja digitar mais CPF? (s/n): ')
    if continuar == 's' or continuar == 'S':
        continue
    elif continuar == 'n' or continuar == 'N':
        condicao = False
        os.system('cls')
        print('Fim.')