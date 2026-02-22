class Carro():

    #Constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Encapsulacion
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo = self.__chequeoInterno()

        if (self.__enMarcha and chequeo):
            return "El carro esta en marcha"
        elif(self.__enMarcha and chequeo == False):
            return "No pasó el chequeo interno, no se puede arrancar"
        else:
            return "El carro esta parado"

    def estado(self):
        print("El carro tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y largo de ", self.__largoChasis)

    #Metodo encapsulado
    def __chequeoInterno(self):
        print("Realizando chequeo interno...")

        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if(self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False

miCarro = Carro()
miCarro2 = Carro()

print(miCarro.arrancar(True))
miCarro.estado()

print("\nUn segundo carro ")
print(miCarro2.arrancar(False))
miCarro2.estado()