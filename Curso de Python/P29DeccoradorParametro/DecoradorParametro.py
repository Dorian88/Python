def funcionDecoradora(funcionParametro):
    def funcionInterior(*args, **kwargs):
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        funcionParametro(*args, **kwargs)
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcionInterior

@funcionDecoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcionDecoradora
def resta(num1, num2):
    print(num1 - num2)

@funcionDecoradora
def potencia (base, exponente):
    print(pow(base, exponente))


suma(7, 5, 8)
resta(12, 10)
potencia(base = 5, exponente = 3)