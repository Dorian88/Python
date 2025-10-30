import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.optimize import fsolve

# ------------------------------
# Función para crear evaluadores
# ------------------------------
def crearFuncion(expr):
    contexto = {}

    for k in dir(math):
        if not k.startswith("__"):
            contexto[k] = getattr(math, k)
    for k in dir(np):
        if not k.startswith("__"):
            contexto[k] = getattr(np, k)

    def f(*args):
        if len(args) == 1:
            x = args [0]
            return eval(expr, {"__builtins__": {}}, {**contexto, "x": x})
        elif len(args) == 2:
            x, y = args
            return eval (expr, {"__builtins__": {}}, {**contexto, "x": x, "y": y})
        else:
            raise ValueError("La funcion solo acepta 1 o 2 variables")

    return f

# --------------------
# Entrada de funciones
# --------------------
print("Ingrese la funcion objetivo f(x, y): ")
f_str = input("f(x, y) = ")
print("ingrese la restriccion g(x, y): ")
g_str = input("g(x, y) = ")

f_eval = crearFuncion(f_str)
g_eval = crearFuncion(g_str)

# ---------------------------------
# Sistema de eciaciones de Lagrange
# ---------------------------------
def sistema(vars):
    x, y, lmbd = vars

    #Derivadas parciales
    h = 1e-6
    df_dx = (f_eval(x + h, y) - f_eval(x - h, y))/(2 * h)
    df_dy = (f_eval(x, y + h) - f_eval(x, y - h)) / (2 * h)

    dg_dx = (g_eval(x + h, y) - g_eval(x - h, y)) / (2 * h)
    dg_dy = (g_eval(x, y + h) - g_eval(x, y - h)) / (2 * h)

    return [
        df_dx + lmbd * dg_dx,
        df_dy + lmbd * dg_dy,
        g_eval(x, y)
    ]

# -------------------
# Resolver el sistema
# ___________________

sol_inicial = [1.0, 1.0, 1.0] # Punto inicial
solucion = fsolve(sistema, sol_inicial)

x_sol, y_sol, lmbd_sol = solucion
f_sol = f_eval(x_sol, y_sol)

criticos = [(x_sol, y_sol, f_sol)]

print("\n ---------- Puntos Criticos Encontrados ----------")

for i, (xi, yi, fi) in enumerate(criticos, start = 1):
    print(f"Punto {i}: (x = {xi:.5f}, y = {yi:.5f}) -> f = x = {fi:.5f}")

# ----------------------------
# Seleccion de Maximo / Minimo
# ----------------------------

opcion = input("\n Desea encontrar el Maximo o el Minimo? (max/min): ").strip().lower()

if opcion == "max":
    mejor = max(criticos, key = lambda t: t[2])
elif opcion == "min":
    mejor = min(criticos, key=lambda t: t[2])
else:
    mejor = None
    print("Opcion no valida")

if mejor:
    print(f"\n >>> El {opcion} se da en (x = {mejor[0]:.5f}, y = {mejor[1]:.5f}) con f = {mejor[2]:.5f}")

# -------
# Grafica
# -------
X = np.linspace(-2, 2, 400)
Y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(X, Y)
Z = g_eval(X, Y)

plt.contour(X, Y, Z, levels = [0], colors = "blue") #Restriccion

# --------------------------
# Marcar los puntos Criticos
# --------------------------
for xi, yi, fi in criticos:
    plt.plot(xi, yi, "ro")
    plt.text(xi + 0.05, yi + 0.05, f"f = {fi:.2f}", color = "red")

# Marcar el mejor punto
if mejor:
    plt.plot(mejor[0], mejor[1], 'gs', markersize = 10, label = f"{opcion} encontrado")
    plt.text(mejor[0] + 0.1, mejor[1] + 0.1,f"({mejor[0]:.2f}, {mejor[1]:.2f})\n", color="green")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Metodo de Multiplicadores de Lagrange")
plt.legend()
plt.show()