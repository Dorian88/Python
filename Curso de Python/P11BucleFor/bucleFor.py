#Usando el bucle for

for i in [1, 2, 3]:
    print(i,"Hola", end=" - ")

print("\n")

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i)

print("\n-----------------VALIDANDO EMAIL-----------------")

contador = 0
miEmail = input("Ingrese una dirección de email: ")

for i in miEmail:
    if(i == "@" or i == "."):
        contador = contador + 1

if contador == 2:
    print("Email correcto")
else:
    print("El email no es correcto")

print("\n-----------------USANDO RANGE-----------------")

for i in range(5):
    print("Dorian", end = " ")
    print(f"Valor de la variable {i}")

print("\n-----------------VALIDANDO EMAIL USANDO RANGE-----------------")
valido = False
email = input("Introduce tu Email: ")

for i in range(len(email)):
    if email[i] == 0:
        valido = True

if valido:
    print("El email es correcto")
else:
    print("El email es incorrecto")