import matplotlib.pyplot as plt
import numpy as np

#Definir la funcion
def crearFuncion(expr):
    def f(x):
        return eval(expr, {"__builtins__": {}}, {"x": x, "np": np})

    return f

#Metodo de la biseccion
def biseccion(f, a, b, tol = 1e-6, max_iter = 100):

    if f(a)*f(b) >= 0:
        raise ValueError("La funcion no cambia de signo en el intervalo dado")

    # Listas para guardar datos de la grafica
    iteraciones = []
    errores = []
    aproximaciones = []

    # encabezado de la tabla
    print(f"{'iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(a)':<12}{'f(b)':<12}{'f(c)':<12}{'f(a)f(b)':<12}{'f(a)f(c)':<12}{'Error':<12}")

    for i in range (max_iter):
        c = (a + b) / 2 #Punto medio
        fa, fb, fc = f(a), f(b), f(c)
        error = abs(fc)

        # Guardar datos para graficar
        iteraciones.append(i+1)
        errores.append(error)
        aproximaciones.append(c)

        # Muestra la fila de la tabla
        print(f"{i+1:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fa:<12.6f}{fb:<12.6f}{fc:<12.6f}{fa*fb:<12.6f}{fa*fc:<12.6f}{error:<12.6f}")

        #Si se encuentra la raiz o se alcanza la tolerancia
        if error < tol or (b - a) / 2 < tol:
            print (f"\nraiz aproximada: ", c)
            return c, iteraciones, errores, aproximaciones

        # Elegir el nuevo intervalo
        if f(a)*fc < 0:
            b = c
        else:
            a = c

    print("\nSe alcanzo el numero maximo de iteraciones")
    return (a + b) / 2

#Se llama el metodo
expr = input("Ingrese la funcion f(x): ")
f = crearFuncion(expr)

a = float(input("Ingrese el limite inferior del intervalo: "))
b = float(input("Ingrese el limite superior del intervalo: "))

raiz, iteraciones, errores, aproximaciones = biseccion(f, a, b, tol = 1e-6)

#*****************************
# Graficas en la misma ventana
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (8, 10))

#**********************
# Grafica de la funcion
#**********************

x = np.linspace(a - 2, b + 2, 400)
y = f(x)

ax1.plot(x, y, label = "f(x)")
ax1.axhline(0, color = "black", linestyle = "-")
ax1.scatter(raiz, f(raiz), color = "red", label = f"Raiz Aprox = {raiz:.6f}")
ax1.text(raiz, f(raiz), f"{raiz:.6}", color = "black", fontsize = 10, ha = "left", va = "bottom")
ax1.set_title("Funcion f(x) y Aproximacion de la raiz")
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.legend()

#******************
# Grafica del error
#******************
ax2.plot(iteraciones, errores, marker = "o", linestyle = "-", color = "blue")
ax2.set_yscale("log") # Escala logaritmica para ver la convergencia
ax2.set_title("Convergencia del error |f(c)| en cada iteracion")
ax2.set_xlabel("Iteraciones")
ax2.set_ylabel("Error")

plt.tight_layout()
plt.show()