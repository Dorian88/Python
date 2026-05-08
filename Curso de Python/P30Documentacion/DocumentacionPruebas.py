import doctest

def areaTriangulo(base, altura):
    """Calcula el área de un triángulo dado
    >>> areaTriangulo(3, 6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4, 5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo(9, 3)
    'El área del triángulo es: 13.5'
    """

    return "El área del triángulo es: " + str((base * altura) / 2)
    #return (base * altura) / 2

print(areaTriangulo(2, 4))

print("-----------------------------Otro ejemplo-----------------------------")
def compruebaMail(mailUsuario):
    """La función compruebaMail evalúa un mail recibido
    en busca de la @. si tiene una @ es correcto,
    si tiene mas de una @ es incorrecto
    si la @ esta al final es incorrecto

    >>> compruebaMail("doaljari@gmail.com")
    True

    >>> compruebaMail("doaljarigmail.com@")
    False

    >>> compruebaMail("doaljarigmail.com")
    False

    >>> compruebaMail("doaljari@gmail.com@")
    False
    """

    arroba = mailUsuario.count('@')

    if(arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0):
        return False
    else:
        return True

doctest.testmod()