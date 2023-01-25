


texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."


def splitTexto(contenido:str):
    textoSplit = contenido.split(" ")
    print(textoSplit)

def joinTexto(contenido:str):
    textoJoin = '-'.join(contenido)
    print(textoJoin)


def countTexto(contenido:str):
    textoCount = contenido.count("texto")
    print(textoCount)


def findTexto(contenido:str):
     textoFind = contenido.find("texto")
     print(textoFind)

def upperTexto(contenido:str):
     textoUpper = contenido.upper()
     print(textoUpper)


def lowerTexto(contenido:str):
     lowerTexto = contenido.lower()
     print(lowerTexto)

if __name__ == '__main__':
    splitTexto(texto)

    joinTexto(texto)

    countTexto(texto)

    findTexto(texto)

    upperTexto(texto)

    lowerTexto(texto)