import sympy as sp

def analisisSensibilidad(B, A, c, b):
    """"
    B: matriz base (nxn)
    A: matriz del problema (nxm)
    c: vector de coeficientes de la FO (mx1)
    b: vector lado derecho (nx1)
    """

    print("\n===MATRIZ BASE===")
    sp.pprint(B)

    # ------------------------
    # Calcular la inversa de B
    # ------------------------
    B_inv = B.inv()
    print("\n===MATRIZ INVERSA DE B===")
    sp.pprint(B_inv)

    # -----------------
    # Variables Basicas
    # -----------------
    X_basic = B_inv * b
    print("\n===SOLUCIÓN BÁSICA===")
    sp.pprint(X_basic)


    # --------------------------
    # Coeficientes de la base CB
    # --------------------------

    base_indices = []
    for i in range(B.shape[1]):
        col = B[:, i]
        for j in range(A.shape[1]):
            if col == A[:, j]:
                base_indices.append(j)

    CB = c[base_indices, :]
    print("\n====COEFICIENTES DE LA BASE C_B====")
    sp.pprint(CB)

    # ----------------
    # Funcion Objetivo
    # ----------------
    Z = CB.T * X_basic
    print("\n===FUNCIÓN OBJETIVO Z===")
    sp.pprint(Z)

    # ------------------------
    # Análisis de sensibilidad
    # ------------------------
    print("\n===CONDICIONES PARA EL RANGO PERMITIDO DE B===")
    condiciones_b = [expr >= 0 for expr in X_basic]
    for cnd in condiciones_b:
        sp.pprint(cnd)

    # ----------------
    # Costos reducidos
    # ----------------
    reduced_costs = (CB.T * B_inv * A) - c.T
    print("\n===COSTOS REDUCIDOS===")
    sp.pprint(reduced_costs)

    # ------------------------
    # Condicion de optimalidad
    # ------------------------
    print("\n===CONDICIONES PARA MANTENER LA MISMA BASE OPTIMA===")
    condiciones_c = [expr >= 0 for expr in reduced_costs]
    for cnd in condiciones_c:
        sp.pprint(cnd)

    return {
        "B_inv": B_inv,
        "X_basic": X_basic,
        "Z": Z,
        "cond_b": condiciones_b,
        "reduced_costs": reduced_costs,
        "cond_c": condiciones_c
    }

# -------
# Ejemplo
# -------
x1, x2, s1, s2 = sp.symbols('x1 x2 s1 s2')
c1, c2, c3, c4 = sp.symbols('c1 c2 c3 c4')
b1, b2 = sp.symbols('b1 b2')

A = sp.Matrix([
    [2, 1, 1, 0],
    [1, 1, 0, 1]
])

B = sp.Matrix([
    [1, 1],
    [0, 1]
])

c = sp.Matrix([c1, c2, c3, c4])

b = sp.Matrix([b1, b2])

resultados = analisisSensibilidad(B, A, c, b)