import math
import matplotlib.pyplot as plt
import numpy as np

#Evaluador de la funcion ingresada
def crearFuncion(expr):
    # Diccionario con todas las funciones y constantes de math
    contexto = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(expr, {"__builtins__": {}}, {**contexto, "x":x})
    return f

def interpolacionCuadratica(f, x0, x1, x2, objetivo = "max", tol = 1e-6, maxIter = 100):

    print(f"{'iter':<6}{'x0':<10}{'f(x0)':<12}{'x1':<10}{'f(x1)':<12}"
          f"{'x2':<10}{'f(x2)':<12}{'x3':<10}{'f(x3)':<12}"
          f"{'error 1':<12}{'error 2':<12}{'error 3':<12}")

    errores = []
    aproximaciones = [x0, x1, x2]

    for it in range(1, maxIter + 1):
        f0, f1, f2 = f(x0), f(x1), f(x2)

        numerador = (f0 * (x1**2 - x2**2) +
                     f1 * (x2**2 - x0**2) +
                     f2 * (x0**2 - x1**2))
        denominador = (2 * (f0 * (x1 - x2) +
                            f1 * (x2 - x0) +
                            f2 * (x0 - x1)))

        if denominador == 0:
            print("El denominador es cero, no se puede continuar")
            return None, None

        x3 = numerador / denominador
        f3 = f(x3)

        # Calculo de errores
        e1 = abs(x3 - x0)
        e2 = abs(x3 - x1)
        e3 = abs(x3 - x2)
        maxError = max(e1, e2, e3)

        errores.append(maxError)
        aproximaciones.append(x3)

        # Muestra la fila de la tabla
        print(f"{it:<6}{x0:<10.6f}{f0:<12.6f}{x1:<10.6f}{f1:<12.6f}"
              f"{x2:<10.6f}{f2:<12.6f}{x3:<10.6f}{f3:<12.6f}"
              f"{e1:<12.6f}{e2:<12.6f}{e3:<12.6f}")

        # Verifica la convergencia
        if maxError < tol:
            return x3, f3, errores, aproximaciones

        # Actualiza los puntos segun objetivo (max o min)
        if objetivo == "max":
            if f3 > f1:
                if x3 > x1:
                    x0 = x1
                    x1 = x3
                else:
                    x2 = x1
                    x1 = x3
            else:
                if x3 > x1:
                    x2 = x3
                else:
                    x0 = x3
        else: # Objetivo = "min"
            if f3 < f1:
                if x3 > x1:
                    x0 = x1
                    x1 = x3
                else:
                    x2 = x1
                    x1 = x3
            else:
                if x3 > x1:
                    x2 = x3
                else:
                    x0 = x3

    return x1, f(x1), errores, aproximaciones

def graficar(f, aproximaciones, errores, xOpt, fOpt):
    fig, axs = plt.subplots(2, 1, figsize = (8, 8))

    # Definir rango dinamico segun las aproximaciones
    xmin, xmax = min(aproximaciones), max(aproximaciones)
    margen = 0.2 * (xmax - xmin if xmax != min else 1)
    xs = np.linspace(xmin - margen, xmax + margen, 400)
    ys = [f(x) for x in xs]

    # Grafica de la funcion
    axs[0].plot(xs, ys, label = "f(x)")
    axs[0].axhline(0, color = "black", linewidth = 0.8)
    axs[0].scatter(aproximaciones, [f(x) for x in aproximaciones], color = "red", label = "Aproximaciones")
    axs[0].scatter(xOpt, fOpt, color = "green", marker = "*", s = 200, label = f"Optimo ≈ {xOpt:.6f}")
    axs[0].set_title("Funcion")
    axs[0].legend()

    # Grafica del error
    axs[1].plot(range(1, len(errores) + 1), errores, marker = "o")
    axs[1].set_title("Error")
    axs[1].set_xlabel("Iteracion")
    axs[1].set_ylabel("Error maximo")

    plt.tight_layout()
    plt.show()

# ******************
# Programa principal
# ******************
if __name__ == "__main__":
    # entrada de la funcion
    expr = input("Ingrese la funcion enterminos de x (ejemplo: 2*sin(x) - x**2/10: ")
    f = crearFuncion(expr)

    # Pregunta si busca maximo o minimo
    objetivo = input("Desea hallar el minimo (min) o el maximo (max)?: ").strip().lower()

    # Puntos iniciales
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    x2 = float(input("Ingrese x2: "))

    # ejecuta el metodo
    xOpt, fOpt, errores, aproximaciones = interpolacionCuadratica(f, x0, x1, x2, objetivo = objetivo)

    print(f"\nEl optimo aproximado en x = {xOpt:.6f}")
    print(f"f(x) = {fOpt:.6f}")

    graficar(f, aproximaciones, errores, xOpt, fOpt)