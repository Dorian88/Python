from tkinter import *

raiz = Tk()

raiz.title("Frame 1")
raiz.iconbitmap(r"C:\Users\USUARIO\Documents\Python\Curso de Python\Interfaces Graficas\Imagenes\Mario.ico")
raiz.geometry("650x350")
raiz.config(bg = "green")

miFrame = Frame()
miFrame.pack()
miFrame.config(bg = "red")
miFrame.config(width = "550", height = "250")
miFrame.config(bd = "35")
miFrame.config(relief = "groove")
miFrame.config(cursor = "pirate")

raiz.mainloop()