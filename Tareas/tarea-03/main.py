from lib.pregunta2 import *
from lib.pregunta3 import *
from lib.pregunta4 import Catalogo,ProductO
from lib.pregunta5Modulo import division,sumaRecursiva
from lib.pregunta6 import * 
from lib.pregunta7 import *


if __name__ == '__main__':
     
     #pregunta2
     
    texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."

    splitTexto(texto)
    joinTexto(texto)
    countTexto(texto)
    findTexto(texto)
    upperTexto(texto)
    lowerTexto(texto)

    print("--------------------------------------------------------------------------------------------------------------")
    #pregunta3

    numero = 10
    print(porValorMultiplicacion(numero))
    print(numero)

    #####################################################################################

    listaNumero = [10]
    print(porReferenciaMultiplicacion(listaNumero))
    print(listaNumero)

    print("--------------------------------------------------------------------------------------------------------------")
    #pregunta4

    catalogo = Catalogo()

    producto1 = ProductO("Chasis","350","nacional")
    producto2 = ProductO("Sistema de frenos","400","importado")
    producto3 = ProductO("Motor","1250","importado")


    catalogo.agregarProducto(producto1)
    catalogo.agregarProducto(producto2)
    catalogo.agregarProducto(producto3)

    catalogo.mostrarProductos()

    
    print("--------------------------------------------------------------------------------------------------------------")
    #pregunta6

    imprimirArchivoEjecucion()
    print("--------------------------------------------------------------------------------------------------------------")
    #pregunta7

    producto = Producto("Motor Audi", "ARGENTINA-0015-2023")
    print(producto) 
    print(producto.identificarPais()) 
    print(producto.identificarLote()) 


