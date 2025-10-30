import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import itertools

# ======================
# MÉTODO SIMPLEX GRÁFICO
# ======================

def simplex_grafico():
    print("\n-------Método Simplex Gráfico-------")

    # Variables simbólicas
    x1, x2 = symbols('x1 x2', real=True)

    # Tipo de optimización
    tipo = input("Desea maximizar o minimizar la función objetivo? (max/min): ").strip().lower()

    # Función objetivo
    z_str = input("Ingrese la función objetivo: ").lower().replace("z =", "").strip()
    a1, a2 = [float(term.split('*x')[0]) for term in z_str.split('+')]

    # Restricciones
    n = int(input("Ingrese el número de restricciones: "))
    restricciones = []
    for i in range(n):
        r = input(f"Restricción {i + 1} : ").strip().replace(" ", "")
        restricciones.append(r)

    # Incluir restricciones de no negatividad
    restricciones.append("x1>=0")
    restricciones.append("x2>=0")

    # Convertir restricciones a ecuaciones simbólicas
    ecuaciones = []
    desigualdades = []
    for r in restricciones:
        if "<=" in r:
            lhs, rhs = r.split("<=")
            desigualdades.append((lhs, "<=", rhs))
            ecuaciones.append(Eq(eval(lhs), float(rhs)))
        elif ">=" in r:
            lhs, rhs = r.split(">=")
            desigualdades.append((lhs, ">=", rhs))
            ecuaciones.append(Eq(eval(lhs), float(rhs)))
        elif "=" in r:
            lhs, rhs = r.split("=")
            desigualdades.append((lhs, "=", rhs))
            ecuaciones.append(Eq(eval(lhs), float(rhs)))

    # Buscar intersecciones entre todas las combinaciones de restricciones
    puntos = []
    for comb in itertools.combinations(ecuaciones, 2):
        sol = solve(comb, (x1, x2), dict=True)
        if sol:
            x_val, y_val = float(sol[0][x1]), float(sol[0][x2])
            if np.isfinite(x_val) and np.isfinite(y_val):
                puntos.append((x_val, y_val))

    # Filtrar puntos dentro de la región factible
    factibles = []
    for (px, py) in puntos:
        valido = True
        for (lhs, op, rhs) in desigualdades:
            lhs_val = eval(lhs, {"x1": px, "x2": py})
            rhs_val = float(rhs)
            if op == "<=" and lhs_val > rhs_val + 1e-6:
                valido = False
            elif op == ">=" and lhs_val < rhs_val - 1e-6:
                valido = False
        if valido and px >= 0 and py >= 0:
            factibles.append((round(px, 4), round(py, 4)))

    # Evaluar función objetivo en cada punto
    resultados = []
    for (px, py) in factibles:
        z = a1 * px + a2 * py
        resultados.append((px, py, z))

    # Determinar Óptimo
    if tipo == "max":
        optimo = max(resultados, key=lambda x: x[2])
    else:
        optimo = min(resultados, key=lambda x: x[2])

    # Mostrar resultados
    print("\n----------RESULTADOS----------")
    print("Puntos factibles:")
    for (px, py, z) in resultados:
        print(f" ({px}, {py}) -> Z = {z:.2f}")
    print(f"\n✅ Solución óptima: x1 = {optimo[0]}, x2 = {optimo[1]}, Z = {optimo[2]:.2f}")

    # ----------------------
    # GRAFICAR RESTRICCIONES
    # ----------------------
    plt.figure(figsize=(8, 6))
    x_vals = np.linspace(0, 20, 400)

    # Dibujar cada restricción
    for (lhs, op, rhs) in desigualdades[:-2]:  # sin las de no negatividad
        expr = solve(Eq(eval(lhs), float(rhs)), x2)
        if expr:
            y_vals = [float(expr[0].subs(x1, xv)) for xv in x_vals]
            plt.plot(x_vals, y_vals, label=f"{lhs}{op}{rhs}")

    # Sombrear región factible correctamente (polígono cerrado)
    if factibles:
        # Ordenar puntos de la región factible por ángulo polar para formar polígono cerrado
        factibles_np = np.array(factibles)
        centro = factibles_np.mean(axis=0)
        angulos = np.arctan2(factibles_np[:,1] - centro[1], factibles_np[:,0] - centro[0])
        orden = np.argsort(angulos)
        factibles_ordenados = factibles_np[orden]

        plt.fill(
            factibles_ordenados[:,0],
            factibles_ordenados[:,1],
            color='green',
            alpha=0.4,
            label='Región Factible'
        )

    # Marcar vértices y punto óptimo
    plt.scatter([p[0] for p in factibles], [p[1] for p in factibles],
                color='blue', label='Vértices Factibles')
    plt.scatter(optimo[0], optimo[1],
                color='red', s=80, label='Óptimo', zorder=5)

    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Método Simplex Gráfico")
    plt.legend()
    plt.show()

# =========
# EJECUCIÓN
# =========

if __name__ == "__main__":
    simplex_grafico()