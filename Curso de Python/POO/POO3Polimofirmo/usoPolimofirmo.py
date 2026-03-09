class Carro():
    def desplazamiento(self):
        print("Me desplazo usando 4 llantas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 llantas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 llantas")


def desplazamientoVehiculos(vehiculo): #Se hace uso de polimofirsmo
    vehiculo.desplazamiento()

miVehiculo1 = Camion()
desplazamientoVehiculos(miVehiculo1)

miVehiculo2 = Carro()
desplazamientoVehiculos(miVehiculo2)

miVehiculo3 = Moto()
desplazamientoVehiculos(miVehiculo3)