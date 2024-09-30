import numpy as np 
import matplotlib.pyplot as plt 
import os
import timeit
import datetime as dt 
import random


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype = int)
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O valor está vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
                
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0
        
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
                
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        
        self.valores[posicao] = valor
        self.ultima_posicao += 1
        
capacidade = 10
vetor = VetorOrdenado(capacidade)
for _ in range(vetor.capacidade):
    vetor.insere(random.choice(range(100)))
    
plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(vetor.capacidade):
    plt.plot(i*vetor.valores[i], i, vetor.valores[i])
plt.legend(vetor.valores)
plt.ylabel('Random')
plt.xlabel('Values')