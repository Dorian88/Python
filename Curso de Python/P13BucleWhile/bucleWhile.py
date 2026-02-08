import math

print ("-------EJEMPLO BÁSICO-------")
i = 1

while i <= 10:
    print ("Ejecución " + str(i))
    i = i + 1

print ("Terminó de ejecutar el bucle while")

print ("\n-------EJEMPLO EVALUANDO LA EDAD-------")

edad = int (input("Introduce tu edad por favor: "))

while edad < 0 or edad > 100:
    print ("Has indtroducido una edad negativa. Por favor vuelva intentarlo")
    edad = int(input("Introduce tu edad por favor: "))

print ("Gracias por colaborar. Puedes pasar")
print ("La edad del aspirante es: " + str(edad))

print ("\n-------EJEMPLO EVALUANDO LA RAIZ CUADRADA DE UN NÚMERO-------")
numero = int(input("Introduce un número por favor: "))
intentos = 0

while numero < 0:
    print ("No se puede hallar la raiz de un número negativo")

    if intentos == 2:
        print("Haz consumido demasiados intentos. El programa ha finalizado")
        break

    numero = int(input("Introduce un número por favor: "))

    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print ("La raiz cuadrada de " + str(numero) + " es " + str(solucion))