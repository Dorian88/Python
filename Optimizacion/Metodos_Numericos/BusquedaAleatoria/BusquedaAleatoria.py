import math
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as slt
from PIL.ImageChops import offset
from mpl_toolkits.mplot3d import Axes3D

# =======================
# Evaluador de la funcion
# =======================
def crearFuncion(expr):
    contexto = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x, y):
        return eval(expr, {"__builtins__":{}}, {**contexto, "x":x, "y":y})
    return f

# ===============================
# Metodo de la busqueda aleatoria
# ===============================
def busquedaAleatoria(expr, xl, xu, yl, yu, nIter, modo = "max"):
    f = crearFuncion(expr)

    if modo == "max":
        mejor = float("-inf")
    else:
        mejor = float("inf")

    mejorx, mejory = None, None

    print(f"{'iter':<10}{'x':<15}{'y':<15}{'f(x, y):<15'}")

    xs, ys, fs = [], [], []

    for i in range(nIter + 1):
        x = xl + (xu - xl) * random.random()
        y = yl + (yu - yl) * random.random()
        val = f(x, y)

        xs.append(x)
        ys.append(y)
        fs.append(val)

        print(f"{i:<10}{x:<15.6}{y:<15.6}{val:<15.6}")

        if modo == "max":
            if val > mejor:
                mejor, mejorx, mejory = val, x, y
            else: # Modo "min"
                if val < mejor:
                    mejor, mejorx, mejory = val, x, y

    return mejorx, mejory, mejor, xs, ys, fs

# =======
# Grafica
# =======
def graficar(expr, xl, xu, yl, yu, xs, ys, fs, mejorx, mejory, mejor, modo):
    f = crearFuncion(expr)

    X = np.linspace(xl, xu, 100)
    Y = np.linspace(yl, yu, 100)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111, projection="3d")

    # Superficie
    ax.plot_surface(X, Y, Z, cmap = "viridis", alpha=0.7)

    # Aproximaciones
    ax.scatter(xs, ys, fs, color = "red", label = "Aproximaciones")

    # Optimo encontrado
    opt_label = "Maximo" if modo == "max" else "Minimo"
    ax.scatter(mejorx, mejory, mejor, color = "green", s = 100, marker = "*", label = f"{opt_label} ≈ {mejor:.4f}")

    # Etiqueta del optimo en la grafica
    offset_z = (max(Z.flatten()) - min(Z.flatten())) * 0.3
    ax.text(mejorx, mejory, mejor + offset_z, f"{opt_label}\n({mejorx:.2f}, {mejory:.2f}, {mejor:.2f})",
            color = "black", fontsize = 10, ha = "center", va = "bottom", backgroundcolor = "white")
    ax.plot([mejorx, mejorx], [mejory, mejory], [mejor, mejor + 2], color = "black", linestyle = "--")

    ax.set_title("Funcion")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.legend()
    plt.show()

# ==================
# Programa Principal
# ==================
if __name__ == "__main__":
    expr = input("ingrese la funcion f(x, y): ")
    xl = float(input("ingrese el limite inferior de x: "))
    xu = float(input("ingrese el limite superior de x: "))
    yl = float(input("ingrese el limite inferior de y: "))
    yu = float(input("ingrese el limite superior de y: "))
    nIter = int(input("ingrese el numero de iteraciones: "))
    modo = input("Desea maximizar o minimizar? (max/min): ").strip().lower()

    mejorx, mejory, mejor, xs, ys, fs = busquedaAleatoria(expr, xl, xu, yl, yu, nIter, modo)
    print(f"\n{('Maximo' if modo == 'max' else 'Minimo')} encontrado en x = {mejorx:.6f}, y = {mejory:.6f}, f(x, y) = {mejor:.6f}")
    graficar(expr, xl, xu, yl, yu, xs, ys, fs, mejorx, mejory, mejor, modo)