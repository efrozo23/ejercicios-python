'''
    Método de regla falsa
    by Elkin Rozo
'''


from math import *


def f(x):
    return log(x**2)-0.7


def falsi(a, b, tol):
    a_n = a
    b_n = b
    # delta = 1
    error = 100
    n = 1
    print("Esto es regla falsa")
    while error > tol:
        c_n = b_n-(f(b_n)*(b_n-a_n))/(f(b_n)-f(a_n))
        if f(a_n)*f(b_n) >= 0:
            print("El metodo de falsa posición falló.")
            return None
        elif f(c_n) == 0:
            print(
                "La solucion exacta fue encontrada: c_n={0:.16f}".format(c_n))
            return c_n
        elif f(a_n)*f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n
        c_new = b_n-(f(b_n)*(b_n-a_n))/(f(b_n)-f(a_n))
        # delta = abs(c_new-c_n)
        error = abs((c_new-c_n)/c_new)*100
        # print("n={0:<2}, c_n={1:.4f}, f(c_n)={2:.4f}, delta={3:.4f}".format(n, c_n, f(c_n), error))
        print("n={0:<2}, c_n={1:.4f}, f(c_n)={2:.4f}, porcentaje={3:.4f}".format(n, c_n, f(c_n), error))
        n += 1
    return c_n


def biseccion(a, b, tol):
    a_n = a
    b_n = b
    n = 1
    # Error absoluto, diferencia entre el valor y el valor anterior
    # delta = 1
    # Error relativo porcentual
    error = 100
    print("Esto es bisección")
    while error > tol:
        c_n = (a_n+b_n)/2.0
        if f(a_n)*f(b_n) >= 0:
            print("El metodo de bisección falló.")
            return None
        elif f(c_n) == 0:
            print("La solucion exacta fue encontrada: c_n={0:.16f}".format(c_n))
            return c_n
        elif f(a_n)*f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n
        c_new = (a_n+b_n)/2.0
        # delta = abs(c_new-c_n)
        error = abs((c_new-c_n)/c_new)*100
        print("n={0:<2}, c_n={1:.16f}, f(c_n)={2:.16f}".format(n, c_n, f(c_n)))
        n += 1
    return c_n


falsi(0.5, 2, 1)
biseccion(0.5, 2, 1e-4)
