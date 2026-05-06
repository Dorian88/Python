def funcionDecoradora(funcionParametro):
    def funcionInterior():
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        funcionParametro()
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcionInterior

@funcionDecoradora
def suma():
    print(15 + 20)

@funcionDecoradora
def resta():
    print(30 - 10)

suma()
resta()