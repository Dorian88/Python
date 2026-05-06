import re

nombre1 = "Dorian Jaramillo"
nombre2 = "Diana Betancur"
nombre3 = "Alexader Rivas"

cadena1 = "Jara López"
cadena2 = "5457543082"
cadena3 = "a545754308"

codigo1 = "sdhrdfjkasñlfhdjks71ghsidjflkvnñsoddfj"
codigo2 = "sdhrdf71jkasñlf hdjksghsidjflkvnñso ddfj"
codigo3 = "sdhrd fjkas ñl fhdjksgh si djflkvnñsoddfj"

print("Función Match")
if re.match("Dorian", nombre1, re.IGNORECASE):
    print("Nombre encontrado")
else:
    print("Nombre no encontrado")

if re.match(r"\d", cadena2):
    print("Número encontrado")
else:
    print("Número no encontrado")

print("\nFunción Search")
if re.search("Jaramillo", nombre1, re.IGNORECASE):
    print("Nombre encontrado")
else:
    print("Nombre no encontrado")

if re.search("71", codigo3):
    print("Código encontrado")
else:
    print("Código no encontrado")
