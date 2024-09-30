import matplotlib.pyplot as plt
import numpy as np 
import os

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(capacidade, dtype = int)
        self.listavetor = []
        self.listaposicao = []
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio')
            return
        else:
            os.system('cls')
            for i in range(self.ultima_posicao + 1):
                plt.plot(vetor.listaposicao, vetor.listaposicao,  vetor.listavetor[i] * vetor.listaposicao[i])
                # plt.plot(self.listavetor, self.listavetor[i], self.listaposicao[i])
                print(f'Posição {i} - {self.vetor[i]}')
    
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade + 1:
            print('Limite do vetor alcançado')
            return
        self.ultima_posicao += 1
        self.vetor[self.ultima_posicao] = valor
        self.listavetor.append(valor)
        self.listaposicao.append(valor)
    
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.vetor[i] == valor:
                print('Valor encontrado.')
                print(f'Posição {i} - {self.vetor[i]}')

    def excluir(self, valor):
        if self.ultima_posicao == -1:
            print('Não há valor para ser excluído')
            return
        for i in range(self.ultima_posicao + 1):
            if self.vetor[i] == valor:
                x = i
                while x <= self.ultima_posicao:
                    self.vetor[x] = self.vetor[x + 1]
                    x += 1
        self.ultima_posicao -= 1
                

vetor = VetorOrdenado(10)
vetor.inserir(2)
vetor.inserir(4)
vetor.inserir(6)
vetor.inserir(8)
vetor.inserir(10)
vetor.imprime()
plt.legend(vetor.listaposicao)

