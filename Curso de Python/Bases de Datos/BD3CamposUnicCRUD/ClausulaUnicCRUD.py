#Cómo crear campos claves

import sqlite3

miConexion = sqlite3.connect("GestionProductos2")
miCursor = miConexion.cursor()

#Oprecaciones CRUD
#Operacion Create
miCursor.execute('''
    CREATE TABLE PRODUCTOS3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica"),
    ("Pantalónes", 15, "Confección")
]

miCursor.executemany("INSERT INTO PRODUCTOS3 VALUES (NULL, ?, ?, ?)", productos)

#Operacion Read
miCursor.execute("SELECT * FROM PRODUCTOS3 WHERE SECCION = 'Confección'")
productos = miCursor.fetchall()
print(productos)

#Operación Update
miCursor.execute("UPDATE PRODUCTOS3 SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'Pelota'")

#Operación Delete
miCursor.execute("DELETE FROM PRODUCTOS3 WHERE ID = 5")

miConexion.commit()
miConexion.close()