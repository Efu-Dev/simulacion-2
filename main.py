

from random import random

def funcion(x):
    return 3*x**2 + 2*x

A = 2 # Límite inferior
B = 3 # Límite superior

def integral_matematica():
    return (B**3+B**2)-(A**3+A**2)

def error(x):
    valor_real = integral_matematica()
    return abs(valor_real-x)/valor_real*100

M = int(input("Ingrese la cantidad de veces que se ejecutará la simulación: "))
suma = 0
for x in range(M):
    xn = random() * (B - A) + A # Genera un número aleatorio entre A y B
    suma += funcion(xn)

valor_aproximado = suma*(B-A)/M

print(f"Resultado Matemático: {integral_matematica()}")
print(f"Resultado Aproximado de la Integral (MonteCarlo): {valor_aproximado}")
print(f"Porcentaje de error: {error(valor_aproximado)}%")