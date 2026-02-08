print ("-------INSTRUCCIÓN CONTINUE-------")

nombre = "Pildoras Informáticas"
contador = 0

for letra in "Phyton":

    if letra == "h":
        continue

    print ("Viendo la letra: " + letra)

for i in nombre:
    if i == " ":
        continue
    contador += 1

print (contador)

print ("\n-------INSTRUCCIÓN ELSE-------")

email = input("Introduce su correo por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print (arroba)