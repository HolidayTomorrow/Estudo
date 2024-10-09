# class Conta:
#     def __init__(self, saldo):
#         self.saldo = saldo
#     def set_saldo(self, saldo):
#         if(saldo <0):
#             print("Saldo não pode ser negativo")
#         else:
#             self.saldo = saldo
# conta1 = Conta(200.0)
# print(conta1.saldo)
# conta2 = Conta(300.0)
# print(conta2.saldo)
# conta3 = Conta(100.0)
# conta3.set_saldo(-100.0)
# print(conta3.saldo)
# conta1.saldo = -100.0
# print(conta1.saldo)

class Conta:
    def __init__(self, saldo = 0.0):
        self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print('Saldo não pode ser negativo')
        else:
            self._saldo = saldo

conta1 = Conta(200.0)
print(conta1.saldo)
conta2 = Conta(300.0)
print(conta2.saldo)
conta2.saldo = -100.0
print(conta2.saldo)

