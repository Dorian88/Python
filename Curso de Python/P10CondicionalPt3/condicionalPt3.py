#Programa que otorga Becas

print("Programa de Becas")

distanciaEscuela = int(input("Introduce la distancia a la escuela en Km: "))
numeroHermanos = int(input("Introduce el número de hermanos: "))
salarioFamiliar = int(input("Introduce el salario anual de la familia: "))

print("La distancia de su casa a la escuela es de: ", distanciaEscuela)
print("El número de hermanos es de: ", numeroHermanos)
print("El salario de la familia es de: ", salarioFamiliar, " Al año.")

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    print("\nTienes derecho a beca")
else:
    print("\nNo tienes derecho a beca.")