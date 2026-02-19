#Ejemplo de excepciones
def suma(num1, num2):
    return num1 + num2

def resta(num3, num4):
    return num3 - num4

def multiplicacion(num5, num6):
    return num5 * num6

def division(num7, num8):

    try:
        return num7 / num8
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
        return "Operación Erronea"

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion = input("Introduce la operación que deseas realizar (suma, resta, multiplicación, división): ")

if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplicacion":
    print(multiplicacion(op1, op2))
elif operacion == "division":
    print(division(op1, op2))
else:
    print("Operación no completada")

print("Oparacion completada. Continua el programa")