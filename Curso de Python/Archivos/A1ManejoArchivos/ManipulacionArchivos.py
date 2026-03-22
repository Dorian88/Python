from io import open

print("1. Se crea el texto en modo escritura y se escribe en el una frase con la funcion write()."
      "\nEsto se hace con la letra w en la función open como 2° argumento")
archivoTexto = open("archivo.txt", "w")
frase = '"Dos cosas son infinitas: la estupidez humana y el universo; y no estoy seguro de lo segundo" \nAlbert Einstein'
archivoTexto.write(frase)

print("\n2. Se accede al archivo en modo lectura y se extrae la información con la función read()."
      "\nEsto se hace con la letra r en la función open como 2° argumento")
archivoTexto = open("archivo.txt", "r")
texto = archivoTexto.read()

print("\n3. Se accede al archivo en modo lectura y se lee la información por lineas con la función readlines()."
      "\nEsto también se hace con la letra r en la función open como 2° argumento")
archivoTexto = open("archivo.txt", "r")
lineasTexto = archivoTexto.readlines()

print("\n4. Se agrega una nueva linea al archivo, De nuevo se hace con la funcion write()."
      "\nEsto se hace con la letra a en la función open como 2° argumento")
archivoTexto = open("archivo.txt", "a")
archivoTexto.write("\nFísico Alemán")

print("\n5. Posicionar el cursor en algun lugar del archivo, Se hace con la funcion seek().")
archivoTexto = open("archivo.txt", "r")
print(archivoTexto.read())
archivoTexto.seek(11)
print(archivoTexto.read(), "\n")

print("\n6. Para abrirlo como lectura y escritura, en el segundo argumento se adiciona r+.")
archivoTexto = open("archivo.txt", "r+")
archivoTexto.write("Comienzo del texto ")
print(archivoTexto.read(), "\n")


archivoTexto.close()
print(texto)
print(lineasTexto)
