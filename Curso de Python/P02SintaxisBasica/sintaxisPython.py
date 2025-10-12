#Muestra de ka sitaxis basica del curso lenguaje

print("Los operadores son\n")
print("-----------ARITMETICOS-----------")
print("Suma: (+)\nResta: (-)\nMultiplicación: (*)\nDivisión: (/)\nPotencia: (**)\nMódulo: (%)\n")

print("-----------EJEMPLOS-----------")
print("a = 5,  b = 6\n")
a = 5
b = 6

print("Suma a + b")
res = a + b
print("El resultado suma es: ", res, "\n")

print("Resta  a - b")
res = a - b
print("El resultado la resta es: ", res, "\n")

print("Multiplicación a * b")
res = a * b
print("El resultado de la multiplicación es: ", res, "\n")

print("División a / b")
res = a / b
print("El resultado la división es: ", res, "\n")

print("Potencia a ** b")
res = a ** b
print("El resultado la potencia es: ", res, "\n")

print("Módulo a % b")
res = a % b
print("El resultado del módulo es: ", res, "\n")

print("-----------OPERADORES DE COMPARACIÓN-----------")
print("Mayor que: (>)\nMenor que: (<)\nMayor o igual que: (>=)\nMenor o igual que: (<=)")
print("Igual que: (==)\n")

print("-----------EJEMPLOS-----------")
print("a = 5,  b = 6, c = 7, d = 7\n")
a = 5; b = 6; c = 7; d = 7

print("Mayor que: b > a")
if (b > a):
    print("b es mayor que b\n")

print("Menor que: a < b")

if (a < b):
    print("a es menor que b\n")

print("Mayor o igual que: a >= b")
if (b >= a):
    print("a es mayor o igual que b\n")

print("Menor o igual que: a <= b")
if (a <= b):
    print("a es menor o igual que b\n")

print("Operador igual: c == d", " c = 7, d = 7")
if (c == d):
    print("c y d son iguales\n")

print("-----------OPERADORES LÓGICOS-----------")
print("Operador Y: (and)\nOperador O: (or)\nOperador no: (not)\n")

print("-----------EJEMPLOS-----------")
print("temperatura = 25 y estaSoleado = True\n")
temperatura = 25; estaSoleado = True; tieneSombrilla = False

print("Operador Y: temperatura > 20 and estaSoleado")
if (temperatura > 20 and estaSoleado):
    print("Es un día perfecto para salir de picnic\n")

print("Operador O: estaSoleado or tieneSombrilla")
if (estaSoleado or tieneSombrilla):
    print("Vamos a caminar\n")

print("Operador no: not estaSoleado")
estaSoleado = False
if not estaSoleado:
    print("Sería mejor quedarnos en casa\n")