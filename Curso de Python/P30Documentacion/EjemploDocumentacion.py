class Areas:

    """Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areaCuadrado (lado):

        """Calcula el área del cuadrado
        elevando al cuadrado el lado pasado por parámetro"""

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """Calcula el área del triángulo
        utilizando los parámetros base y altura"""

        return "El área del triángulo es: " + str((base * altura)/2)

print(Areas.areaCuadrado(5))
print(Areas.areaCuadrado.__doc__)
help(Areas.areaCuadrado)
print(Areas.areaTriangulo(7, 5))
help(Areas.areaTriangulo)

help(Areas)