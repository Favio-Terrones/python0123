

def porValorMultiplicacion(x):
    x = x * 2
    return x

def porReferenciaMultiplicacion(x):
    x[0] = x[0] * 2
    return x[0]

if __name__ == '__main__':
    numero = 10
    print(porValorMultiplicacion(numero))
    print(numero)


#####################################################################################


    listaNumero = [10]
    print(porReferenciaMultiplicacion(listaNumero))
    print(listaNumero)