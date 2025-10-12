#Ejemplos de funciones

def mensaje():
    print("Estoy aprendiendo Python")
    print("Hasta ahora voy en las instrucciones básicas")
    print("Poco a poco voy avanzando")

mensaje()

print("\nEjecutando fuera de la función")
mensaje()


def suma():
    num1 = 5
    num2 = 7

    print("El resultado es: ", num1 + num2)

def suma1(num1, num2):
    print("El resultado es: ", num1 + num2)

def suma2(num1, num2):
    resultado = num1 + num2
    print("El resultado es: ", resultado)

print("\nFunción sin parametros")
suma()

print("\nFunción con parametros")
suma1(35, 358)

print("\nFunción con return")
suma2(2, 3)