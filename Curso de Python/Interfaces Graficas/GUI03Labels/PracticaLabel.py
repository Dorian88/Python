from tkinter import *

root = Tk()

root.iconbitmap(r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Mario.ico")
root.title("Practicando con Label")

miFrame = Frame(root, width = 500, height = 400)
miFrame.pack()

miImagen = PhotoImage(file = r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Jesucristo.png")

Label(miFrame, image = miImagen).place(x = 200, y = 250)
Label(miFrame, text = "Otro mundial sin Italia", fg = "blue", font = ("Verdana" , 18)).place(x = 100, y = 200)

root.mainloop()
