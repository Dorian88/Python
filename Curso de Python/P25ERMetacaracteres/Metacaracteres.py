import re

listaNombres = [
    'Dorian Jaramillo',
    'Edwin Jaramillo',
    'Mario Jaramillo',
    'Laura Jaramillo'
]

listaUrl = [
    'https://ww3.animeonline.ninja',
    'https://lossimpson-tvlatino.blogspot.com',
    'https://www.poketvlatino.com',
    'http://live2.mystreamplayer.com'
]

listaPalabras = [
    'Hombres',
    'Mujeres',
    'Mascotas',
    'Niños',
    'Niñas'
]

print("^ Para los que inician")
for elemento in listaNombres:
    if re.findall('^Laura', elemento): #^ Para los que inician
        print(elemento)

print("\n")
for elemento in listaUrl:
    if re.findall('^https', elemento): #^ Para los que inician
        print(elemento)

print("\n$ Para los que terminan")
for elemento in listaNombres:
    if re.findall('Jaramillo$', elemento):
        print(elemento)

print("\n")
for elemento in listaUrl:
    if re.findall('com$', elemento):
        print(elemento)

print("\n[] Para buscar un caracter en particular")
print("Buscamos los que tienen el caracter n")
for elemento in listaNombres:
    if re.findall('[n]', elemento):
        print(elemento)

print("\nBuscamos los que tienen el caracter ñ")
for elemento in listaPalabras:
    if re.findall('[ñ]', elemento):
        print(elemento)
