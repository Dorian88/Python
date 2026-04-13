from tkinter import *

raiz = Tk()

raiz.iconbitmap(r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Calculadora.ico")
raiz.title("Calculadora")

miFrame = Frame(raiz)
miFrame.pack()

numeroPantalla = StringVar()
resetPantalla = False
operacion = ""
resultado = 0
num1 = 0
contadorResta = 0
contadorMulti = 0
contadorDiv = 0
#---------------------PANTALLA-------------------------------
pantalla = Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(background = "black", fg = "#03f943", justify = "right")

#---------------------FUNCIONALIDAD DE LA CALCULADORA-------------------
#---------------------Pulsaciones teclado-------------------------------
def numeroPulsado(num):
    global operacion, resetPantalla

    if resetPantalla != False:
        numeroPantalla.set(num)
        resetPantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#---------------------Metodo Suma-------------------------------
def suma(num):
    global operacion, resultado, resetPantalla

    resultado += int(num)
    operacion = "suma"
    resetPantalla = True
    numeroPantalla.set(resultado)

#---------------------Metodo Resta-------------------------------
def resta(num):
    global operacion, resultado, num1, contadorResta, resetPantalla

    if contadorResta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contadorResta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorResta += 1
    operacion = "resta"
    resetPantalla = True

#---------------------Metodo Multiplicación-------------------------------
def multiplicacion(num):
    global operacion, resultado, num1, contadorMulti, resetPantalla

    if contadorMulti == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contadorMulti == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorMulti = contadorMulti +1
    operacion = "multiplicacion"
    resetPantalla = True

#---------------------Metodo División-------------------------------
def division(num):
    global operacion, resultado, num1, contadorDiv, resetPantalla

    if contadorDiv == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contadorDiv == 1:
            resultado = num1 * float(num)
        else:
            resultado = num1 / float(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorDiv = contadorDiv + 1
    operacion = "division"
    resetPantalla = True

#---------------------Metodo Igual-------------------------------
def igual():
    global resultado, operacion, contadorResta, contadorMulti, contadorDiv

    if operacion == "suma":
        numeroPantalla.set(int(resultado) + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contadorResta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contadorMulti = 0
    elif operacion == "division":
        numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
        resultado = 0
        contadorDiv = 0

#---------------------BOTONES-------------------------------
#---------------------Fila 1-------------------------------
boton7 = Button(miFrame, text = "7", width = 3, command = lambda : numeroPulsado("7"))
boton7.grid(row = 2, column = 1)
boton8 = Button(miFrame, text = "8", width = 3, command = lambda : numeroPulsado("8"))
boton8.grid(row = 2, column = 2)
boton9 = Button(miFrame, text = "9", width = 3, command = lambda : numeroPulsado("9"))
boton9.grid(row = 2, column = 3)
botonDividir = Button(miFrame, text = "/", width = 3, command = lambda  : division(numeroPantalla.get()))
botonDividir.grid(row = 2, column = 4)

#---------------------Fila 2-------------------------------
boton4 = Button(miFrame, text = "4", width = 3, command = lambda : numeroPulsado("4"))
boton4.grid(row = 3, column = 1)
boton5 = Button(miFrame, text = "5", width = 3, command = lambda : numeroPulsado("5"))
boton5.grid(row = 3, column = 2)
boton6 = Button(miFrame, text = "6", width = 3, command = lambda : numeroPulsado("6"))
boton6.grid(row = 3, column = 3)
botonMultiplicar = Button(miFrame, text = "x", width = 3, command = lambda  : multiplicacion(numeroPantalla.get()))
botonMultiplicar.grid(row = 3, column = 4)

#---------------------Fila 3-------------------------------
boton1 = Button(miFrame, text = "1", width = 3, command = lambda : numeroPulsado("1"))
boton1.grid(row = 4, column = 1)
boton2 = Button(miFrame, text = "2", width = 3, command = lambda : numeroPulsado("2"))
boton2.grid(row = 4, column = 2)
boton3 = Button(miFrame, text = "3", width = 3, command = lambda : numeroPulsado("3"))
boton3.grid(row = 4, column = 3)
botonRestar = Button(miFrame, text = "-", width = 3, command = lambda  : resta(numeroPantalla.get()))
botonRestar.grid(row = 4, column = 4)

#---------------------Fila 5-------------------------------
botonComa = Button(miFrame, text = ",", width = 3, command = lambda : numeroPulsado(","))
botonComa.grid(row = 5, column = 1)
boton0 = Button(miFrame, text = "0", width = 3, command = lambda : numeroPulsado("0"))
boton0.grid(row = 5, column = 2)
botonIgual = Button(miFrame, text = "=", width = 3, command = lambda  : igual())
botonIgual.grid(row = 5, column = 3)
botonSumar = Button(miFrame, text = "+", width = 3, command = lambda  : suma(numeroPantalla.get()))
botonSumar.grid(row = 5, column = 4)

raiz.mainloop()