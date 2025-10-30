import math
import matplotlib.pyplot as plt
import numpy as np

def razonDorada(f, xl, xu, tol = 1e-6, maxIter = 100, mode = "min"):
    phi = 0.618 # Razon Dorada

    errores = [] # Lista para graficar el error
    puntosX = [] # Puntos candidatos de cada iteracion
    puntosY = []

    # Encabezado de la tabla
    print(f"{'Iter':<5}{'xl':<12}{'xu':<12}{'d':<12}{'x1':<12}{'x2':<12}{'f(x1)':<12}{'f(x2)':<12}{'Error':<12}")

    for i in range(1, maxIter + 1):
        # Cálculo de los puntos en cada iteración
        d = phi * (xu - xl)
        x1 = xl + d
        x2 = xu - d

        f1, f2 = f(x1), f(x2)
        error = abs(x2 - x1)

        # Guardar datos para graficar
        xMid = (x1 + x2)/2
        puntosX.append(xMid)
        puntosY.append(f(xMid))
        errores.append(error)

        # Mostrar fila de la tabla
        print(f"{i:<5}{xl:<12.6}{xu:<12.6}{d:<12.6}{x1:<12.6}{x2:<12.6}{f1:<12.6}{f2:<12.6}{error:<12.6}")

        if error < tol:
            break

        # Actualizacion segun minimo o maximo
        if mode == "max": # Busqueda del minimo
            if f2 > f1:
                xu = x1
            else:
                xl = x2
        else: # Busqueda del minimo
            if f2 < f1:
                xu = x1
            else:
                xu = x1

    x_opt = (xl + xu)/2
    f_opt = f(x_opt)

    return x_opt, f_opt, errores, puntosX, puntosY

#====================
# Programa Principal
#====================
if __name__ == "__main__":
    func_str = input("Ingrese la funcion en terminos de x (Ej: 2*sin(x) - (x**2/10): ")

    # Se crea la funcion evaluable con acceso directo a math
    def f(x):
        return eval(func_str, {"x":x, **math.__dict__})

    # Intervalo de Búsqueda
    xl = float(input("Ingrese el limite inferior del intervalo: "))
    xu = float(input("Ingrese el limite superior del intervalo: "))
    mode = input("Desea buscar el 'min' (minimo) o 'max' (maximo): ").strip().lower() # Modo de busqueda

    # Ejecución del método
    x_opt, f_opt, errores, puntosX, puntosY = razonDorada(f, xl, xu, mode = mode)

    print(" \n======RESULTADO FINAL======")
    if mode == "min":
        print(f"Minimo aproximado en x ≈ {x_opt}, f(x) ≈ {f_opt}")
    else:
        print(f"Maximo aproximado en x ≈ {x_opt}, f(x) ≈ {f_opt}")

    #*********
    # Graficas
    #*********
    fig, axs = plt.subplots(2, 1, figsize = (8, 10))

    # Grafica de la funcion
    margen = (xu - xl) * 2
    X = np.linspace(xl - margen, xu + margen, 800)
    Y = [f(x) for x in X]

    axs[0].plot(X, Y, label = "f(x)")
    axs[0].scatter(x_opt, f_opt, color="green", marker="*", s=200,
                   zorder=5, label=f"Optimo ≈ {x_opt:.4f}")
    axs[0].annotate(f"{f_opt:.4f}", (x_opt, f_opt), textcoords="offset points",
                    xytext=(0, 10), ha="center", color="green")
    #axs[0].scatter(x_opt, f_opt, color = "red", zorder = 5, label=f"Optimo ({x_opt:.4f}, {f_opt:.4f})")
    #axs[0].annotate(f"{f_opt:.4f}", (x_opt, f_opt), textcoords="offset points", xytext=(0, 10), ha="center", color="red")
    axs[0].set_title("Funcion")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("f(x)")
    axs[0].legend()

    # Grafica del error
    axs[1].plot(range(1, len(errores) + 1), errores, marker = "o")
    axs[1].set_title("Error")
    axs[1].set_xlabel("Iteracion")
    axs[1].set_ylabel("error")

    plt.tight_layout()
    plt.show()