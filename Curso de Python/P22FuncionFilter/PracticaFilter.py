def numeroPar(num):
    if num % 2 == 0:
        return True

numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numeroPar, numeros)))

print("\nMezclando las funciones lambda y filter")

print(list(filter(lambda numeroPar: numeroPar % 2 == 0, numeros)))

print("\n+++++++++++++++++++EJEMPLO+++++++++++++++++++")

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleado("Dorian", "Presidente", 5000000),
    Empleado("Diana", "Gerente", 4500000),
    Empleado("Edwin", "RRHH", 4000000),
    Empleado("Luisa", "Administrativo", 3500000),
    Empleado("Mario", "Secretario", 3000000)
]

salariosAltos = filter(lambda empleado: empleado.salario > 3500000, listaEmpleados)

for empleadoSalario in salariosAltos:
    print(empleadoSalario)