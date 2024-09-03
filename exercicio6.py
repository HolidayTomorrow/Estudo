# Exercício
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplica(multiplicado):
    def multiplicador(numero):
        return numero * multiplicado
    return multiplicador

duplicar = multiplica(2)
triplicar = multiplica(3)
quadruplica = multiplica(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplica(2))
        




