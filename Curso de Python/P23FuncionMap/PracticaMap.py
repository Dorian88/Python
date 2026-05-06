class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}US$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleado("Dorian", "Presidente", 6700),
    Empleado("Diana", "Gerente", 7500),
    Empleado("Edwin", "RRHH", 2100),
    Empleado("Luisa", "Administrativo", 2150),
    Empleado("Mario", "Secretario", 1800)
]

def calculoComision(empleado):

    if(empleado.salario <= 3000):
        empleado.salario = empleado.salario * 1.03

    return empleado

listaEmpleadoComision = map(calculoComision, listaEmpleados)

for empleado in listaEmpleadoComision:
    print(empleado)