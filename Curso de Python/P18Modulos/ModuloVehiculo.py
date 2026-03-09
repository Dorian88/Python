class Vehiculos():

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

 #Así se hereda
class Moto(Vehiculos):
    picando = ""

    def pique(self):
        self.picando = "Estoy haciendo piques"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.picando)

class Camioneta(Vehiculos):
    def cargar(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La camioneta está cargada"
        else:
            return "La camioneta no esta cargada"

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargaElecttrica(self):
        self.cargando = True

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miMoto = Moto("Honda", "CBR")
miCamioneta = Camioneta("Renault", "Kangoo")
miBici = BicicletaElectrica("Orbea", "Thj")

print("Para la moto")
miMoto.pique()
miMoto.estado()

print("\nPara la camioneta")
miCamioneta.arrancar()
miCamioneta.estado()
print(miCamioneta.cargar(True))

print("\nPara la bicicleta")