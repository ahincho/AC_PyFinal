
from tkinter import *

# Variables Globales para el Tamanio y Fuente

sizeScreen = "400x235"
fontLabel = "Century Gothic"

# Variables Globales para algunos Colores

colorWhite = "#f4f5f4"
colorBlack = "#101010"

# Variables Globales para algunos Colores de Elementos

colorBackground = "#151515"
colorButton = "#303030"

# Metodo Auxiliar para insertar un Espacio o Salto de Linea
# El Metodo recibe una pantalla para aplicar un Salto de Linea

def getEnter(screen):
    Label(screen, text = "", bg = colorBackground).pack()

# Metodo que crea un Cuadro de Dialogo o Ventana para los Botones

def newScreen(screen, text):
    screen.title(text)
    screen.geometry(sizeScreen)
    screen.configure(bg = colorBackground)
    Label(screen, text = f"¡{text}!", fg = colorWhite, bg = colorBlack, font = (fontLabel, 18), width = "500", height = "2").pack()

# Metodo usado por el Comando o Accion 'Register', se activara
# al cliquear el Boton 'Registrarse' de la pantalla principal

def register():
    global user1
    global user_entry1
    global screen1

    # Creamos la nueva pantalla a la 'altura' de la Principal
    screen1 = Toplevel(mainScreen)

    newScreen(screen1, "Registrarse")

# Metodo Principal o Main del Programa

mainScreen = Tk()
mainScreen.geometry(sizeScreen)
mainScreen.title("Sistema de Reconocimiento Facial")
mainScreen.configure(bg = colorBackground)

Label(text = "¡Bienvenido!", fg = colorWhite, bg = colorBlack, font = (fontLabel, 18), width = "500", height = "2").pack()

getEnter(mainScreen)

Button(text = "Iniciar Sesion", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), width = "40", command = "").pack()

getEnter(mainScreen)

Button(text = "Registrarse", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), width = "40", command = register).pack()

mainScreen.mainloop()
