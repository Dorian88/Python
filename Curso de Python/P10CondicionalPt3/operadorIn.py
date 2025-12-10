#Asignacion de materias electivas

print("Materias electivas año 2025:")
print("Informática gráfica - Pruebas de Software - Usabilidad y Accesibildad")

opcion = input("Escriba la materia a matricular: ")

asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y Accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print ("La asignatura escogida no está en la lista")