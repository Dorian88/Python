#Cómo crear campos claves

import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS2 VALUES (NULL, ?, ?, ?)", productos)

#miCursor.execute("INSERT INTO PRODUCTOS2 VALUES ('AR05', 'Tren', 15, 'Juguetería')")

miConexion.commit()
miConexion.close()