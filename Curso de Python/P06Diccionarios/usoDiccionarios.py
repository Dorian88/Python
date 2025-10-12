# Usando Diccionarios

print("Sintaxis del diccionarios: nombreDiccionario = {clave1:valor1, ..., claven:valorn}\n")

miDiccionario = {"Colombia":"Bogotá", "Venezuela":"Caracas", "Brasil":"Brasilia"}
print("Los elementos del diccionario son: ", miDiccionario)

print("\nPara ver un elemento del diccionario se usa la clave: diccionario[clave]")
print("La capital de Colombia es: ", miDiccionario["Colombia"])

print("\nPara agregar un elemento al diccionario: diccionario[clave] = valor")
print("Se ingresa la capital de Perú")
miDiccionario ["Perú"] = "Lima"
print("Ahora el diccionario tiene un nuevo elemento: ", miDiccionario)

print("\nPara eliminar un elemento al diccionario: del diccionario[clave]")
print("Vamos a borrar la pareja Venezuela - Caracas")
del miDiccionario ["Venezuela"]
print("Ahora el diccionario tiene un nuevo elemento: ", miDiccionario)

print("\nEl diccionario puede alternar elementos")
miDiccionario1 = {"Colombia":"Bogotá", "Falcao":9, "Enanos":7}
print("Los elementos del diccionario son: ", miDiccionario1)

print("\nCombinando Tuplas y Diccionarios: tupla[posElem]:valor")
miTupla1 = ["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario2 = {miTupla1[0]:"Madrid", miTupla1[1]:"París", miTupla1[2]:"Londres", miTupla1[3]:"Berlín"}
print("Los elementos del diccionario son: ", miDiccionario2)

print("\nIngresar una tupla completa a un diccionario clave:tupla")
miTupla2 = ["Liga 2007 - 1", "Liga 2007 - 2", "Liga 2024 - 2", "Copa Colombia 2024", "Super Liga 2024"]
miDiccionario3 = {"Nombre":"David", 1:"Ospina", "Equipo":"Atl. Nacional", "Títulos":miTupla2}
print("Los elementos del diccionario son: ", miDiccionario3)

print("\nAlgunos metodos para usar con los diccionarios:")
print("keys(): Muestra las claves del diccionario")
print("values(): Muestra los valores del diccionario")
print("len(): Muestra la cantidad total de elementos del diccionario")


