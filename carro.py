class Carro():
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
class Bateria(Carro):
    def __init__(self):
        pass
    def capacidade(self, wattshora, duracao):
        self.wattshora = wattshora
        self.duracao = duracao
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
        self.bateria = Bateria()

lista_carro =[
    {'Marca': 'Fiat'},
    {'Modelo': 'Uno'},
    {'Cor': 'Vermelho'},
    {'Ano': '2014'}
]

lista_bateria = [
    {'WattsHora': '70KWh'},
    {'Duracao': '10h'},
]

for lista in lista_carro:
    carro = CarroEletrico(lista.get('Marca'), lista.get('Modelo'), lista.get('Cor'), lista.get('Ano'))
carro.bateria.capacidade(lista_bateria[0], lista_bateria[1])
print(carro.marca, carro.modelo, carro.cor, carro.ano, '\n')
print(carro.bateria.wattshora, carro.bateria.duracao)
        
        