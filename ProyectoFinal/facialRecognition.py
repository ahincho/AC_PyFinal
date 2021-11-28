
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
    global userEntry1
    global screen1

    # Creamos la nueva pantalla a la 'altura' de la Principal
    screen1 = Toplevel(mainScreen)
    user1 = StringVar()

    newScreen(screen1, "Registrarse")
    userEntry1 = formConfig(screen1, user1, 0)

# Metodo usado por el Comando o Accion 'Login', se activara al
# cliquear el Boton 'Iniciar Sesion' de la pantalla principal

def login():
    global user2
    global userEntry2
    global screen2

    # Creamos la nueva pantalla a la 'altura' de la Principal
    screen2 = Toplevel(mainScreen)
    user2 = StringVar()

    newScreen(screen2, "Iniciar Sesion")
    userEntry2 = formConfig(screen2, user2, 1)

# Agregar los Labels necesarios para el Registro o Inicio de Sesion
# Diferenciamos si es Registro o Login por la variable 'flag'

def formConfig(screen, user, flag):
    Label(screen, text = "Usuario:", fg = colorWhite, bg = colorBackground, font = (fontLabel, 16)).pack()
    entry = Entry(screen, textvariable = user, justify = CENTER, font = (fontLabel, 16))
    entry.focus_force()
    entry.pack(side = TOP, ipadx = 30, ipady = 6)

    getEnter(screen)

    if flag:
        Button(screen, text = "Capturar Rostro", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), height="2", width="40", command = "").pack()
    else:
        Button(screen, text = "Capturar Rostro", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), height="2", width="40", command = "").pack()
    
    return entry

# Metodo Principal o Main del Programa

mainScreen = Tk()
mainScreen.geometry(sizeScreen)
mainScreen.title("Sistema de Reconocimiento Facial")
mainScreen.configure(bg = colorBackground)

Label(text = "¡Bienvenido!", fg = colorWhite, bg = colorBlack, font = (fontLabel, 18), width = "500", height = "2").pack()

getEnter(mainScreen)

Button(text = "Iniciar Sesion", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), width = "40", command = login).pack()

getEnter(mainScreen)

Button(text = "Registrarse", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 16), width = "40", command = register).pack()

mainScreen.mainloop()
