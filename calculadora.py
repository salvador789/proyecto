#!/usr/bin/python3.8

import fibonnacci

def suma(x,y):
 print("El resultado es: ",x+y)
def resta(x,y):
 print("El resultado es: ",x-y)
def division(x,y):
 print("El resultado es: ",x/y)
def multiplicacion():
 print("El resultado es: ",x*y)

uno=int(input("Ingresa un numero: "))
dos=int(input("Ingresa otro numero: "))

respuesta=int(input("Selecciona el numero de operacion que quieres hacer: \n"
		 "1.-Sumar\n"
		 "2.-Restar\n"
		 "3.-Dividir\n"
		 "4.-Multiplicar\n"
		 "5.-Serie fibonacci\n"))
if respuesta == 1:
 suma(uno,dos)
elif respuesta == 2:
 resta(uno,dos)
elif respuesta == 3:
 division(uno,dos)
elif respuesta == 4:
 multiplicacion(uno,dos)
elif respuesta == 5:
 fibonnacci.fib(uno)
else:
 print("Elejiste una opcion no valida!!")
print("Fin del programa")
