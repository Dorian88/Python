from tkinter import *
from tkinter import filedialog

raiz = Tk()

raiz.iconbitmap(r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Mario.ico")
raiz.title("Abrir Archivos")

def abreArchivo():
    archivo = filedialog.askopenfilename(title = "Abrir", initialdir = "C:", filetypes = (("Archivos Excel", "*.xlsx"),
                                    ("Archivos de texto", "*.txt"),
                                                                                          ("Todos los Archivo", "*.*")))
    print(archivo)

Button (raiz, text = "Abrir Archivo", command = abreArchivo).pack()

raiz.mainloop()