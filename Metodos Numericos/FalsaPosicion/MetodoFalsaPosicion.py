import math
import matplotlib.pyplot as plt
import numpy as np

# Definir la funcion
def crearFuncion(expr):
    contexto = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(expr, {"__builtins__": {}}, {**contexto, "x": x})

    return f

#Metodo de la falsa posicion
def falsaPosicion(f, xl, xu, tol = 1e-6, max_iter = 100):
    if f(xl) * f(xu) > 0:
        raise ValueError("La funcion no cambia de signo en el intervalo dado")

    xrAnterior = None # Variable para calcular el error
    raices = []
    errores = []

    # Encabezado de la tabla
    print(f"{'Iter':<10}{'xl':<12}{'xu':<12}{'xr':<12}{'f(xl)':<12}{'f(xu)':<12}{'f(xr)':<12}{'f(xl)f(r)':<12}{'Error':<12}")

    for i in range(1, max_iter + 1):
        #Ecuacion de la falsa posicion
        xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))

        #Calcular el valor de la funcion en xr
        fxr = f(xr)

        # Calcular el error
        if xrAnterior is None:
            error = None #No hay error en la primera iteracion
        else:
            error = abs(xr - xrAnterior)

        # Guarda los datos para graficar
        raices.append(xr)
        errores.append(error if error is not None else 0)

        # Imprime la fila de la tabla
        print(f"{i:<10}{xl:<12.6f}{xu:<12.6f}{xr:<12.6f}{f(xl):<12.6f}{f(xu):<12.6f}{fxr:<12.6f}{(f(xl) * f(xu)):<15.6f}{'' if error is None else f'{error:.6f}'}")

        #Verificar la tolerancia
        if abs(fxr) < tol:
            return xr, raices, errores

        #Actualizar los xl o xu
        if f(xl) * fxr < 0:
            xu = xr
        else:
            xl = xr

        xrAnterior = xr

    return xr, raices, errores

expr = input("Ingrese la funcion (Ejemplo: x**2 - x - 2, o use funciones de math como sin(x)): ")
xl = float(input("Ingrese el valor de xl: "))
xu = float(input("Ingrese el valor de xu: "))

f= crearFuncion(expr)

raiz, raices, errores = falsaPosicion(f, xl, xu)

print(f"\nLa raiz aproximada es: {raiz:.6f}")

#--------------------
#Graficas
#--------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (8, 8))

#Grafica de la funcion
xVals = np.linspace(xl - 1, xu + 1, 400)
yVals = [f(x) for x in xVals]
ax1.plot(xVals, yVals, label = "f(x)")
ax1.axhline(0, color = "black", linewidth = 0.8)
ax1.scatter(raices, [f(r) for r in raices], color = "red", label = "Aproximaciones")
ax1.scatter(raiz, f(raiz), color = "green", s = 100, marker = "*", label = f"Raiz ≈ {raiz:.6f}")
ax1.annotate(f"{raiz:.6f}", xy=(raiz, f(raiz)), xytext=(raiz + 0.5, f(raiz)),
             arrowprops=dict(facecolor = 'green', shrink = 0.05), fontsize = 9, color = "green")
ax1.set_title("Grafica de la Funcion")
ax1.legend()
#ax1.grid(True)

# Grafica del error
ax2.plot(range(1, len(errores) + 1), errores, marker = "o")
ax2.set_title("Grafica del Error")
ax2.set_xlabel("Iteracion")
ax2.set_ylabel("Error")
#ax2.grid(True)

plt.tight_layout()
plt.show()