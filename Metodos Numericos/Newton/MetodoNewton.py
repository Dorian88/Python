import math
import numpy as np
import matplotlib.pyplot as plt

def crearFuncion(expr):
    contexto = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(expr, {"__builtins__": {}}, {**contexto, "x": x})
    return f

# *****************
# Derivada numerica
# *****************
def derivada(f, x, h = 1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

# ****************
# Metodo de Newton
# ****************
def metodoNewton(f, x0, tol=1e-6, maxIter = 50):
    print("{:<10}{:<15}{:<15}{:<15}{:<15}".format("iter", "x", "f(x)", "f'(x)", "Error"))
    errores, aproximaciones = [], [x0]

    for i in range(maxIter):
        fx = f(x0)
        fpx = derivada(f, x0)
        if fpx == 0:
            print("Derivada nula. No se puede continuar.")
            break
        x1 = x0 - (fx/fpx)
        error = abs(x1 - x0)
        errores.append(error)
        print("{:<10}{:<15.6f}{:<15.6f}{:<15.6f}{:<15.6f}".format(i + 1, x0, fx, fpx, error))
        aproximaciones.append(x1)

        if error < tol:
            break
        x0 = x1

    return aproximaciones, errores

# ********
# Graficas
# ********
def graficar(f, aproximaciones, errores):
    fig, axs = plt.subplots(2, 1, figsize=(8, 8))

    # Grafica de la funcion
    xVals = np.linspace(-10, 20, 400)
    yVals = [f(x) for x in xVals]
    axs[0].plot(xVals, yVals, label = "f(x)")
    axs[0].axhline(0, color = "black", linewidth = 0.8)
    axs[0].scatter(aproximaciones, [f(x) for x in aproximaciones], color = "red", label = "Aproximaciones")
    xOpt = aproximaciones[-1]
    yOpt = f(xOpt)
    axs[0].scatter([xOpt], [yOpt], color="green", s=100, zorder=5, label="Óptimo")
    axs[0].annotate(f"({xOpt:.4f}, {yOpt:.4f})", (xOpt, yOpt),
                    textcoords="offset points", xytext=(10, 10), fontsize=9, color="green")
    axs[0].set_title("Metodo de Newton")
    axs[0].legend()

    # Grafica del error
    axs[1].plot(range(1, len(errores)+1), errores, "ro-")
    axs[1].set_title("Errores")
    axs[1].set_xlabel("Iteracion")
    axs[1].set_ylabel("Error")

    plt.tight_layout()
    plt.show()

# *****************
# Funcion principal
# *****************
if __name__=="__main__":
    expr = input("Ingrese la funcion (Ejemplo: x**3 - 2*x - 5 o 2*sin(x) - x**2/10): ")
    f = crearFuncion(expr)
    x0 = float(input("Ingrese el valor inicial x0: "))

    aproximaciones, errores = metodoNewton(f, x0)
    graficar(f, aproximaciones, errores)