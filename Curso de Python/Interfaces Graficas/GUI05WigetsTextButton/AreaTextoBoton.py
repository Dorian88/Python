from tkinter import *

root = Tk()

root.iconbitmap(r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Mario.ico")
root.title("Practicando con Widgets")

miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()

miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable = miNombre)
cuadroNombre.grid(row = 0, column = 1, padx = 10, pady = 10)
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*")
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 3, column = 1, padx = 10, pady = 10)
textoComentario = Text(miFrame, width = 16, height = 10)
textoComentario.grid(row = 4, column = 1, padx = 10, pady = 10)
scrollVert = Scrollbar(miFrame, command = textoComentario.yview)
scrollVert.grid(row = 4, column = 2, sticky = "nsew")
textoComentario.config(yscrollcommand = scrollVert.set)

nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 10)
apellidoLabel = Label(miFrame, text = "Apellido: ")
apellidoLabel.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)
PassLabel = Label(miFrame, text = "Contraseña: ")
PassLabel.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)
direccionLabel = Label(miFrame, text = "Direccion: ", )
direccionLabel.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 10)
comentariosLabel = Label(miFrame, text = "Comentarios: ", )
comentariosLabel.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10)

def codigoBoton():
    miNombre.set("Dorian")

botonEnvio = Button(root, text = "Enviar", command = codigoBoton)
botonEnvio.pack()

root.mainloop()