'''
    Metodo de Bisección f(x)=0 entre [a,b]
'''
# Parametros de entrada
# n -> número de iteraciones
# t -> criterio de convergencia

# Parametros de salida
# c -> parametro de salida

from math import *


def f(x):
    return x**3 - 4*x*cos(x) + (2*sin(x))**2 -3


def biseccion(a, b, t):
    c_n = (a+b)/2.0
    a_n = a
    b_n = b
    n = 1
    while ((b_n - a_n)/2.0 > t):
        if f(a_n)*f(b_n) >= 0:
            print("El metodo fallo")
            return None
        elif f(c_n) == 0:
            print("Solución exacta fue encontrada:  {0:.16f}".format(c_n))
            return c_n
        elif f(a_n)*f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n
        c_n = (a_n+b_n)/2.0
        print("n={0:<2} , c_n={1:.16f} , f(c_n)={2:.16f}".format(n, c_n, f(c_n)))
        # print("{0:.16f}".format(c_n))
        n += 1
    return c_n


biseccion(1,2, 1e-5)
# print(1e+1)
# print("Valor de funcion: ",f(2))
# print("Valor de funcion: ",f(1))
