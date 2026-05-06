import re

print("------------------------------EJEMPLO 1------------------------------")

cadena1 = "Vamos a aprender expresiones regulares"

print(re.search("aprender", cadena1))

print("\n------------------------------EJEMPLO 2------------------------------")

textoBuscar = "expresiones"

if re.search(textoBuscar, cadena1) is not None:
    print("He encontrado el texto")
else:
    print("no he encontrado el texto")

print("\n------------------------------EJEMPLO 3------------------------------")

texto = "regulares"
textoEncontrado = re.search(texto, cadena1)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

print("\n------------------------------EJEMPLO 4------------------------------")

cadena2 = "Vamos a aprender expresiones regulares en Python. Python es un leguaje de sintaxis sencilla"

buscarTexto = "Python"

print(re.findall(buscarTexto, cadena2))
print(len(re.findall(buscarTexto, cadena2)))