import pickle

listaNombres = ["Dorian", "Diana", "Mario", "Luisa"]
archivoBinario = open("listaNombres", "wb")

pickle.dump(listaNombres, archivoBinario)

archivoBinario.close()

del (archivoBinario)

archivo = open("listaNombres", "rb")
lista = pickle.load(archivo)

print(lista)