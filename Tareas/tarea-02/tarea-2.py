# Favio Alonso Terrones Chinchay



print("\t\tPregunta N°1")


msg = """
     ¿Que deseas hacer hoy?

     1.-Dibujar un cuadrado en consola
     2.-Saber los números multiplos de 2 en una lista 
     3.-Visualizar los mayores de edad de una lista
"""

print(msg)

opcion = int(input("Ingrese una opción: "))

if opcion == 1:
    lado = int(input("Ingrese el lado del cuadrado: "))

    for i in range(lado):
         print('*'*(lado)) 

elif opcion == 2:

    cantidadNumeros = int(input("Digite la cantidad de números que tendra su lista: "))
    numeros = []
    i = 0
    while i<cantidadNumeros :
      i +=1
      numero = int(input("Ingrese un número: "))
      numeros.append(numero)

    print("\t\tLos números multiplos de 2 son: ")
    for numero in numeros:
         if(numero%2==0):
            print(numero)   

elif opcion == 3:

    cantidadPersonas = int(input("Digite la cantidad de personas que tendra su lista: "))
    personas = []

    i=0
    while i<cantidadPersonas:
        i+=1
        persona = []
        nombre = input("\nIngrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        persona.append(nombre)
        persona.append(edad)
        personas.append(persona)

    print("\n\t\tLos mayores de edad son: ")
    for persona in personas:
         if(persona[1]>=18):
              print(persona[0],"->",persona[1])

else: 
      print("Opción no valida")




print("\t\tPregunta N°2")


biblioteca = {
     "categorias": ["cuentos de hadas","aventuras","tragedia","romance","novela policíaca","ciencia ficción"],
      "libros": [
          {
                "nombreLibro":"Caperucita Roja",
                "autor": "Lopez",
                "añoPublicacion": 1784,
                "categoria": "cuento de hadas",
                "estado": "disponible"
          },
         {
                "nombreLibro": "Dune",
                "autor": "Frank Herbert",
                "añoPublicacion": 1954,
                "categoria": "ciencia ficción",
                "estado":"disponible"
          },
          {
               "nombreLibro": "Romeo y Julieta",
               "autor": "William Shakespeare",
               "añoPublicacion": 1597,
               "categoria":"tragedia",
               "estado":"disponible"
          }]
      ,
      "usuarios" : [
            {
               "nombre":"Favio",
               "apellido": "Terrones",
               "dni": "72718154",
            },
            {
                "nombre":"Alan",
                "apellido": "Ñacari",
                "dni": "75651234"
            },
            {
                "nombre":"Johan",
                "apellido":"Silva",
                "dni": "65214598"
            }
      ]
              
}

def obtenerCategorias():
    print(biblioteca["categorias"])


def obtenerNombreYAutorLibros():
      listaLibros = []
      for libro in biblioteca["libros"]:
         listaLibros.append((libro["nombreLibro"],libro["autor"]))
      return listaLibros

def cambiarEstadoLibro(nombre,estado):
      for libro in biblioteca["libros"]:
             if libro["nombreLibro"] == nombre:
                  libro["estado"] = estado
                  print(f"El libro {libro['nombreLibro']} cambio a estado {libro['estado']}")
                  return
      print(f"Libro no encontrado")
      return

def obtenerUsuarios():
       listaUsuarios = []
       for usuario in biblioteca["usuarios"]:
           listaUsuarios.append(usuario["nombre"])
       return listaUsuarios



## OBTENER CATEGORIAS 
 
obtenerCategorias()

## OBTENER NOMBRE Y AUTOR DE LOS LIBROS 

print(obtenerNombreYAutorLibros()) 

## CAMBIAR ESTADO DEL LIBRO

cambiarEstadoLibro("Dune","ocupado")

## OBTENER USUARIOS

print(obtenerUsuarios())



print("\t\tPregunta N°3")


def evaluarNumeroMayor(a,b):
       if a > b :
         return a
       else:
         return b

print(evaluarNumeroMayor(5,15))




print("\t\tPregunta N°4")


import sys

def imprimirArgumentos():
    argumentos = sys.argv 
    for arg in argumentos:
        print(arg)

imprimirArgumentos()     
