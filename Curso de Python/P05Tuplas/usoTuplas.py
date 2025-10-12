# Mostrando como se usa las tuplas en Python

miTupla = ("Dorian", 13, 1, 1995)
print("Mostrando la tupla: ", miTupla)

#Mostrando el elemento 2 de la tupla
print("\nAccediendo al elemento que se encuentra en la posición 2 de la tupla: ", miTupla[2])

print("\nSe puede guardar una tupla en una lista (list)")
miLista = list(miTupla)
print("Mostrando la lista con la tupla : ", miLista)

print("\nDe una lista a una tupla (tuple)")
miLista = ["Daniela" , 23, 2, 1994]
miTupla1 = tuple(miLista)
print("Mostrando la Tupla con la Lista : ", miTupla1)

print("\nBuscando un elemento de la tupla")
print("Se busca el elemento Dorian en la tupla: ", "Dorian" in miTupla)
print("Se busca el elemento 1995 en la tupla: ", 1995 in miTupla1)

print("\nCantidad de un elemento en la tupla")
print("El elemento 1995 está ", miTupla.count(1995), " veces en la tupla")

print("\nCantidad total de la tupla")
print("en la tupla hay un total de ", len(miTupla1), " elementos")

print("\nExtraer los elementos de la tupla en una variable")
nombre, dia, mes, agno = miTupla
print("Nombre: ", nombre, "\nDía: ", dia, "\nMes: ", mes, "\nAño: ", agno)
