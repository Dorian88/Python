# Ejemplo usando condicional elif

print("Verificación de acceso")

notaAlumno = int(input("Introduce tu nota por favor: "))

if notaAlumno < 3:
    print("Tu valoración es insuficiente.")
elif notaAlumno < 4:
    print("Tu valoración es bien")
elif notaAlumno < 6:
    print("Tu valoración es notable")
else:
    print("Nota incorrecta")

print ("\nEl programa ha terminado")