class Persona():
    def __init__(self,nombre, edad, lugarResidencia ):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descricion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de residencia: ",
              self.lugarResidencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado ):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descricion(self):
        super().descricion()
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)

Dorian = Persona("Dorian", 42, "Itagui")
Alex = Empleado(1500, 20, "Alexander", 42, "Itagui")

Dorian.descricion()
print("\n")
Alex.descricion()

print(isinstance(Alex, Persona))