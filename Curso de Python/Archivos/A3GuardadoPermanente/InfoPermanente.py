import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        #return "{} {} {}".format(self.nombre, self.genero, self.edad)
        return f"{self.nombre} {self.genero} {self.edad}"

class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("Archivo Externo", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            #print("Se cargaron {} personas del archivo externo".format(len(self.personas)))
            print(f"Se cargaron {len(self.personas)} personas del archivo externo")
        except:
            print("El archivo esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agragarPersonas(self, p):
        self.personas.append(p)
        self.guardarEnArchivoExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarEnArchivoExterno(self):
        listaDePersonas = open("Archivo Externo", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoArchivo(self):
        print("La informacion del archivo es la siguiente:")

        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona("Luisa", "Femenino", 36)
miLista.agragarPersonas(persona)
miLista.mostrarInfoArchivo()
