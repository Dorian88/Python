from string import printable

areaTriangulo = lambda base, altura: (base * altura)/2

triangulo1 = areaTriangulo(7, 5)
triangulo2 = areaTriangulo(9, 6)

print("El area del triangulo 1 es: ", triangulo1)
print("El area del triangulo 2 es: ", triangulo2)

print("\n----------------EJEMPLO----------------")

alCubo = lambda numero: pow(numero, 3)

print("El cubo del numero 13 es: ", alCubo(13))

print("\n----------------OTRO EJEMPLO----------------")

destacarValor = lambda comision: "¡{}!$".format(comision)

comisionDorian = 250000

print("Dorian tiene una comision de ", destacarValor(comisionDorian))