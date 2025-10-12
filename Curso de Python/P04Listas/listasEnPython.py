#Ejemplos de listas en python

print("Sintaxis de la lista: nombreDeLaLista = [elemento 1, elemento 2,...]")
miLista = ["Dorian", "Diana", "Alexander", "Luisa"]

print("\nPara imprimir toda la lista nombreDeLaLista[:]")
print(miLista [:])

print("\nPara imprimir un elemento de la lista nombreDeLaLista[posicionDelElemento]")
print(miLista [2])

print("\nPara imprimir una porción de la lista nombreDeLaLista[0:3]. Muestra los"
      " tres primeros elementos")
print(miLista [0:3])

print("\nPara agregar un elemento a la lista nombreDeLaLista.append(elemento)."
      " Se agrega al final")
miLista.append("Edwin")
print(miLista [:])

print("\nPara agregar un elemento a la lista nombreDeLaLista.insert(posiciónQueIngresa, elemento)."
      " Se agrega en el punto en que se indique")
miLista.insert(2, "Jennifer")
print(miLista [:])

print("\nPara agregar varios elementos a la lista nombreDeLaLista.extend([elemento1,...])."
      " Se agregan al final")
miLista.extend(["Mario", "Marly", "Samuel"])
print(miLista [:])

print("\nPara averiguar donde se encuentra un elemento dentro de la lista"
      "nombreDeLaLista.index('elemento'")
print("El elemento se encuentra en la posición: ", miLista.index("Diana"))

print("\nPara averiguar si se encuentra un elemento dentro de la lista o no"
      "'Elemento' in lista me muestra true o false")
print("Con elemento Luisa me debería mostrar True y con el elemento Camila me debería"
      "mostrar False")
print("Con Luisa ", "Luisa" in miLista)
print("Con Camila ","Camila" in miLista)

print("La lista puede almacenar cualquier tipo de elemento")
miLista1 = ["Laura", 4, True, 78.43]
print(miLista1[:])

print("\nPara eliminar un elemento de la lista: nombreDeLaLista.remove(elemento)"
      "Vamos a eliminar el elemento '4'")
miLista1.remove(4)
print(miLista1[:])

print("\nListado de otras funciones:\n pop(): elimina el último elemento de la lista\n"
      " Concatenar listas operador +: lista = lista1 + lista2\n Repetidor de listas operador *: "
      " lista = lista1[Elementos]* N° a repetir")
