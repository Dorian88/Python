import sympy as sp
import numpy as np
import pandas as pd

def ingresarDatos():
    print("\n======METODO SIMPLEX ALGEBRAICO======")

    # Variables simbólicas
    vars_str = input("Ingrese los nombres de las variables separadas por un espacio (Ej: x1 x2): ")
    variables = sp.symbols(vars_str)
    n = len(variables)

    # Función Objetivo
    z_expr = sp.sympify(input("Ingrese la función objetivo: "))
    c = np.array([z_expr.coeff(v) for v in variables], dtype = float)

    # Restricciones
    m = int(input("\nIngrese el número de restricciones: "))
    A, b = [], []
    for i in range(m):
        restr = input(f"Restriccion {i+1}: ")
        lhs, rhs = restr.split("<=")
        lhs_expr = sp.sympify(lhs)
        rhs_val = float(rhs)

        if rhs_val < 0:
            raise ValueError("❌ El lado derecho debe ser mayor o igual que 0.")

        A.append([lhs_expr.coeff(v) for v in variables])
        b.append(rhs_val)

    return np.array(c), np.array(A), np.array(b), variables

def simplex(c, A, b, variables):
    m, n = A.shape

    A = A.astype(float)
    b = b.astype(float)
    c = c.astype(float)

    # Agrega variables de holgura
    A = np.hstack([A, np.eye(m)])
    c = np.concatenate([c, np.zeros(m)])
    base = list(range(n, n + m))
    iteracion = 0

    # Construir encabezados de la tabla simplex
    columnas = ["Z"] + [str(v) for v in variables] + [f"s{i + 1}" for i in range(m)] + ["b"]

    #=================TABLA INICIAL=================
    print("\n==========Iteración 0==========")

    #Fila 0
    fila0 = [1] + list(-c) + [0] # Coeficiente de la función objetivo

    # Filas de las restricciones
    filas = []
    for i in range(m):
        filas.append([0] + list(A[i]) + [b[i]])

    # Se une todo
    data = [fila0] + filas
    tabla = pd.DataFrame(data, columns = columnas)

    #Agregar etiquetas de ecuaciones y variables básicas
    ec_labels = [f"({i})" for i in range(m + 1)]
    vb_labels = ["Z"] + [f"s{i + 1}" for i in range(m)]
    tabla.insert(0, "VB", vb_labels)
    tabla.insert(0, "Ec#", ec_labels)

    print(tabla.to_string(index = False))

    # Comienzo de iteraciones
    while True:
        iteracion += 1

        print(f"\n=========== Iteracion {iteracion} ===========")

        cb = c[base]
        zj = np.dot(cb, A)
        cj_zj = zj - c

        cj_zj = np.array([float(val) for val in cj_zj], dtype = float)

        fila0 = [1] + list(np.round(cj_zj, 3)) + [0]

        # Filas de restricciones
        filas_iter = []
        for i in range(m):
            filas_iter.append([0] + list(np.round(A[i], 3)) + [np.round(b[i], 3)])

        data_iter = [fila0] + filas_iter
        tabla_iter = pd.DataFrame(data_iter, columns = columnas)

        #Etiquetas
        ec_labels_iter = [f"({i})" for i in range(m + 1)]
        vb_labels_iter = ["Z"] + [columnas[base[i] + 1] for i in range(m)]
        tabla_iter.insert(0, "VB", vb_labels_iter)
        tabla_iter.insert(0, "Ec#", ec_labels_iter)

        print(tabla_iter.to_string(index = False))

        # Tabla de iteraciones
        #columnas_iter = [str(v) for v in variables] + [f"s{i + 1}" for i in range(m)] + ["b"]
        #tabla_iter = pd.DataFrame(np.column_stack([A, b]), columns = columnas_iter)
        #tabla_iter.insert(0, "VB", [columnas_iter[base[i]] for i in range(m)])
        #fila0 = np.concatenate((["Z"], np.round(cj_zj, 3), [0]))
        #tabla_iter.loc[len(tabla_iter.index)] = fila0
        #print(tabla_iter.to_string(index = False))

        # Mostrar tabla simplex
        #columnas = [str(v) for v in variables] + [f"s{i + 1}" for i in range(m)] + ["b"]
        #tabla = pd.DataFrame(np.column_stack([A, b]), columns = columnas)
        #tabla.insert(0, "VB", [columnas[base[i]] for i in range(m)])
        #print(tabla.to_string(index = False))
        #print("\nZj - Cj: ", np.round(cj_zj, 3))

        # Prueba de optimalidad
        cj_zj_num = np.array([float(x) for x in cj_zj])
        if all(cj_zj_num >= 0):
            print("\n✅ Solución óptima alcanzada.")
            xb = np.zeros(len(c))
            xb[base] = b
            z_opt = np.dot(c, xb)
            print("\nSolución óptima: ")
            for i in range(len(variables)):
                print(f"{variables[i]} = {xb[i]: .2f}")

            print(f"Valor óptimo de Z = {z_opt: .2f}")
            break

        # Variable que entra
        col_pivote = np.argmin(cj_zj)
        print(f"\nVariable que entra: {columnas[col_pivote + 1]}")

        # Prueba de cociente mínimo
        columna = A[:, col_pivote]
        razones = np.divide(b, columna, out = np.full_like(b, np.inf), where = columna > 0)

        if all(columna <= 0):
            print("❌problema no acotado.")
            break

        fila_pivote = np.argmin(razones)
        print(f"Variable que sale: {columnas[base[fila_pivote] + 1]}")

        # Pivoteo
        pivote = A[fila_pivote, col_pivote]
        A[fila_pivote, :] /= pivote
        b[fila_pivote] /= pivote

        for i in range(m):
            if i != fila_pivote:
                factor = A[i, col_pivote]
                A[i, :] -= factor * A[fila_pivote, :]
                b[i] -= factor * b[fila_pivote]

        base[fila_pivote] = col_pivote

# Programa principal
if __name__ == "__main__":
    c, A, b, variables = ingresarDatos()
    simplex(c, A, b, variables)