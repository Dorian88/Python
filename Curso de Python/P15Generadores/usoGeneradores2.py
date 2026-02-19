def devuelveCiudades(*ciudades):

    for elementos in ciudades:
        #for subElemento in elementos:
            yield from elementos

ciudadesDevueltas = devuelveCiudades("Medellín", "Itaguí", "Envigado", "La Estrella")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))