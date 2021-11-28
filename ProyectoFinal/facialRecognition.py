
from tkinter import *

from tkinter import messagebox as msg

# Variables Globales para el tamanio y letra

sizeScreen = "500x250"
fontLabel = "Century Gothic"

mainScreen = Tk()
mainScreen.geometry(sizeScreen)
mainScreen.title("Sistema de Reconocimiento Facial")
mainScreen.configure(bg = "#151515")

Label(text = "¡Bienvenido!", fg = "#f4f5f4", bg = "#101010", font = (fontLabel, 18), width = "500", height = "2").pack()

mainScreen.mainloop()
