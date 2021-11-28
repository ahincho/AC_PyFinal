
from tkinter import *

from tkinter import messagebox as msg

# Variables Globales para el Tamanio y Fuente

sizeScreen = "400x235"
fontLabel = "Century Gothic"

# Variables Globales para algunos Colores

colorWhite = "#f4f5f4"
colorBlack = "#101010"

mainScreen = Tk()
mainScreen.geometry(sizeScreen)
mainScreen.title("Sistema de Reconocimiento Facial")
mainScreen.configure(bg = "#101010")

Label(text = "¡Bienvenido!", fg = colorWhite, bg = colorBlack, font = (fontLabel, 18), width = "500", height = "2").pack()

Button(text = "Iniciar Sesion", fg = colorWhite, bg = "#202020", activebackground = "#151515", borderwidth = 0, font = (fontLabel, 16), width = "40", command = "").pack()

Button(text = "Registrarse", fg = colorWhite, bg = "#202020", activebackground = "#151515", borderwidth = 0, font = (fontLabel, 16), width = "40", command = "").pack()

mainScreen.mainloop()
