nombreUsuario = input("Introduce tu nombre: ")
print("Convirtiendo a mayusculas")
print("Tu nombre es: ", nombreUsuario.upper())

nombreUsuario1 = input("\nIntroduce tu nombre: ")
print("Convirtiendo a minusculas")
print("Tu nombre es: ", nombreUsuario1.lower())

nombreUsuario2 = input("\nIntroduce tu nombre: ")
print("La primera letra mayuscula")
print("Tu nombre es: ", nombreUsuario2.capitalize())

print("\nEjemplo más elaborado para el uso de los String")
edad = input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numérico")
    edad = input("Introduce la edad: ")

if(int(edad) < 18):
    print("No puede pasar")
else:
    print("Puede pasar")