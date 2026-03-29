import pickle

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

carro1 = Vehiculo("Mazda", "MX5")
carro2 = Vehiculo("Seat", "Leon")
carro3 = Vehiculo("Reanult", "Megane")
carros = [carro1, carro2, carro3]
archivo = open("Los Carros", "wb")

pickle.dump(carros, archivo)

archivo.close()

del(archivo)

archivoApertura = open("Los Carros", "rb")
misCarros = pickle.load(archivoApertura)

archivoApertura.close()

for c in misCarros:
    print(c.estado())