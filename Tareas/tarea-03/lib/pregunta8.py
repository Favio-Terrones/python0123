
from pregunta5Modulo import division,sumaRecursiva
import os

while(True):
    try:
        num1 = float(input("Introduce un primer número: "))
        num2 = float(input("Introduce un segundo número: "))

        cantidad = float(input("Ingresa una cantidad de elementos: ")) 

        print(division(num1,num2))
        print(sumaRecursiva(cantidad))
        
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        print(os.getcwd())
        break 
    finally:
        print("Proceso terminado") 
