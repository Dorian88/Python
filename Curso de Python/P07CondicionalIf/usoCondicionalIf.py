#ejemplos usando If

def evaluacion(nota):
    valoracion = "Aprobado"

    if nota < 3:
        valoracion = "No aprobado"

    return valoracion

print(evaluacion(4))

print("\nPrograma de evaluación de notas de alumnos")

notaAlumno = input("Introduce la nota del alumno: ")
print(evaluacion(int(notaAlumno)))