import re

listaNombres = [
    'Ana',
    'María',
    'Rosa',
    'Sandra',
    'Celia'
]

listaCodCiudades = [
    'Ma1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'Va2',
    'Ma4',
    'MaA',
    'Ma5',
    'MaB',
    'MaC'
]

for elemento in listaNombres:
    if re.findall('[o-t]', elemento):
        print(elemento)

print("\n")
for e in listaCodCiudades:
    if re.findall('Ma[0-3]', e):
        print(e)

print("\n")
for e in listaCodCiudades:
    if re.findall('Ma[^0-3]', e):
        print(e)

print("\n")
for el in listaCodCiudades:
    if re.findall('Ma[0-3A-B]', el):
        print(el)