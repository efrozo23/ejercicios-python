'''
    Solución aprox de Newton
    by Elkin Rozo
'''

from math import *


def f(x):
    return x**3 - x**2 + 2

# Derivar la función
# 3*x^x -2*x


def df(x):
    return 3*x**2 - 2*x

# Función que calcula la raíz


def newton(x, tol):
    error = 1
    n = 1
    print("Inicio método de newton")
    while error>tol:
        if df(x) == 0:
            print("Derivada cero.")
            return None
        else:
            h = f(x)/df(x)
            x_new = x-h
            error = abs((x_new)/x_new)*100
            print("n={0:<2}, x ={1:.4f}, f(x)={2:.4f},".format(n,x_new,f(x_new),error))
            x = x_new
            n+=1
    print("El valor de la raiz es x={0:.4f}".format(x))
    return x

