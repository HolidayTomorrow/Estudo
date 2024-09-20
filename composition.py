import datetime
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.now()
        self.transacoes = []
    def imprime(self):
        print(f"data abertura: {self.data_abertura}")
        print("transações: ")
        for t in self.transacoes:
                print("-", t)
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de {valor}")
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        self.saldo -= valor
        self.historico.transacoes.append(f"saque de {valor}")
    def extrato(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        destino.deposita(valor)
        self.historico.transacoes.append(
            f"transferencia de {valor} para conta {destino.numero}"
        )
        return True

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.extrato
conta1.historico.imprime()
conta2.historico.imprime()
