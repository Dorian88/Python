import math
import doctest

def raizCuadrada(listaNumeros):
    """
    La función devuelve una lista con la raiz cuadrada de los elementos
    numéricos pasados por parámetros en otra lista

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = []
    >>> for i in [4, 9, 16, 50, 78, -90, 125]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error



    """

    return [math.sqrt(n) for n in listaNumeros]

print(raizCuadrada([9, 16, 25, 36]))

doctest.testmod()