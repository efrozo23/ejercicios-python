'''
Ejercicio de Secante modificada
'''
from math import *

def f(x): 
    return x**3 - x**2 + 2

def secante(xi,delta,tol):
    n=1
    error=100
    print("Esto es metodo de la secante modificado")
    while error >= tol:
        df=(f(xi + delta * xi)-f(xi))/(delta * xi)
        if df == 0:
            print("Derivada nula. La solucion no fue encontrada.")
            return None
        else:
            h = f(xi)/df 
            # x(i+1) = x(i) - f(x) / f'(x) 
            x_new = xi - h
            error = abs((x_new-xi)/x_new)*100
            print("n={0:<2}, x={1:.4f}, f(x)={2:.4f}, error={3:.4f}".format(n, x_new, f(x_new), error))
            xi = x_new
            n+=1
    print("El valor de la raiz es x={0:.4f}".format(xi))
    return xi

xi = -20  # Valor incial
delta = 0.1
tol = 1
secante(xi,delta,tol)
# print("¡Hello word.!")