# Ejemplos usando concatenando condiciones

edad = 7

if 0 < edad < 100:
    print("edad es correcta")
else:
    print("edad incorrecta")

print("\n---------------EVALUACIÓN DE SALARIOS---------------")
salarioPresidente = int(input("Introduce el salario del presidente: "))
print("El salario del presidente es: " + str(salarioPresidente))
salarioDirector = int(input("\nIntroduce el salario del director: "))
print("El salario del director es: " + str(salarioDirector))
salarioJefeArea = int(input("\nIntroduce el salario del jefe de área: "))
print("El salario del jefe de área es: " + str(salarioJefeArea))
salarioAdministrativo = int(input("\nIntroduce el salario del jefe de área: "))
print("El salario del administrativo es: " + str(salarioAdministrativo))

if salarioAdministrativo < salarioJefeArea < salarioDirector < salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")