from operator import truediv

email = False
miEmail = input("Introduce un email: ")

for i in miEmail:

    if(i == "@"):
        email = True

if (email == True):
    print("Email es correcto")
else:
    print("Email no es correcto")

print("\nUSANDO RANGE")

for i in range(5, 50, 3):
    print ("Hola")
    print (f"El valor de la variable i es: {i + 1}")

print("\nOTRA MANERA DE VALIDAR UN CORREO. EN ESTE CASO USANDO LEN")

valido = False

email1 = input("introduce tu email: ")

for i in range(len(email1)):
    if email1[i] == "@":
        valido = True

if valido:
    print("El email es correcto")
else:
    print("El email no es correcto")