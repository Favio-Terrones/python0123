# Favio Alonso Terrones Chinchay



print("\t\tPregunta N°1")

nombreCompleto = input("¿Cual es tu nombre completo? ")
edad = input("¿Cuantos años tienes? ")
fechaNac = input("¿Cual es tu fecha de nacimiento? ")


print(f"Tu nombre completo es : {nombreCompleto} , con una edad de {edad} años y naciste el {fechaNac}")



print("\t\tPregunta N°2")

pi = 3.14

print("Area del circulo")

radio = float(input("Ingrese el radio: "))

resultado = pi * radio**2
print(f"El área del circulo es: {resultado} ")


print("Area del triangulo")

base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))

resultado = (base*altura)/2
print(f"El área del triangulo es: {resultado} ")


print("Area del cuadrado")

lado = int(input("Ingrese el lado del cuadrado: "))

resultado = lado**2
print(f"El área del cuadrado es: {resultado} ")



print("\t\tPregunta N°3")

numero1 = float(input("Ingrese el 1° numero: "))
numero2 = float(input("Ingrese el 2° numero: "))
numero3 = float(input("Ingrese el 3° numero: "))

suma = numero1 + numero2 + numero3
resta = numero1 - numero2 - numero3
multiplicacion = numero1 * numero2 * numero3
division =   (numero1/numero2)/numero3
divisionEntera = (numero1//numero2)//numero3

print(f"La suma es: {suma}")
print(f"La resta es: {resta} ")
print(f"La multiplicacion: {multiplicacion}")
print(f"La division es: {division}")
print(f"La division entera es: {divisionEntera}")



print("\t\tPregunta N°4")

valor = input("Ingrese un valor: ")

print(f"El tipo de dato es: {type(valor)}")


print("\t\tPregunta N°5")

import sys

variable = sys.argv[0]

print(f"La ubicacion donde me encuentro trabajando es: {variable}")



print("\t\tPregunta N°6")


n = int(input("Ingrese la cantidad de numeros a sumar: "))
sumaNumeros = (n*(n+1))/2
print(f"La suma de los {n} primeros numeros es: {sumaNumeros}")




print("\t\tPregunta N°7")

num1 = int(input("Ingrese el 1er número: "))
num2 = int(input("Ingrese el 2do número: "))

if num1 == num2:
    print(f"Los numeros {num1} y {num2} son iguales")
else :
    if num1 > num2:
        print(f"Los numeros {num1} y {num2} son diferentes y el numero {num1} es mayor a {num2}") 
    else:
        print(f"Los numeros {num1} y {num2} son diferentes y el numero {num1} es menor a {num2}") 



print("\t\tPregunta N°8")


password = "contra123"

passwordInput = input("Ingrese la contraseña: ")

if password == passwordInput:
    print("Las contraseñas coinciden , acceso valido")
else:
    print("Contraseña incorrecta")    