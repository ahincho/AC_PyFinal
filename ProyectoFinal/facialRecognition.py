
from tkinter import *
from tkinter import messagebox as msg

import cv2

import matplotlib.pyplot as plt

from mtcnn.mtcnn import MTCNN

import database as db

import os

# Variable Global para el Path, este debe ser cambiado

path = "C:/Users/Angel/Desktop/ProyectoFinal/"

# Variables Globales para el Tamanio y Fuente

sizeScreen = "400x235"
fontLabel = "Century Gothic"

# Variables Globales para algunos Colores

colorWhite = "#f4f5f4"
colorBlack = "#101010"

# Variables Globales para los colores de los mensajes dentro del sistema

colorSuccess = "\033[1;32;40m"
colorError = "\033[1;31;40m"
colorNormal = "\033[0;37;40m"

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
        Button(screen, text = "Capturar Rostro", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 18), height="2", width="40", command = loginRecording).pack()
    else:
        Button(screen, text = "Capturar Rostro", fg = colorWhite, bg = colorButton, activebackground = colorBackground, borderwidth = 0, font = (fontLabel, 18), height="2", width="40", command = registerRecording).pack()
    
    return entry

# Metodo para tomar una foto en tiempo real usando la Camara Web y OpenCV
# Se encendera la camara web para tomar una foto y asignarla a un usuario
# Este metodo pertenece al Boton Registrarse

def registerRecording():
    cap = cv2.VideoCapture(0)
    userReg = user1.get()
    img = f"{userReg}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Registro Facial", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    userEntry1.delete(0, END)

    pixels = plt.imread(img)
    faces = MTCNN().detect_faces(pixels)
    getFace(img, faces)
    
    # Registrar en base de datos el rostro

    registerFaceOnDB(img)

# Metodo para registrar un rostro dentro de la Base de Datos
# con un usuario previamente ya seleccionado o especificado

def registerFaceOnDB(img):
    nameUser = img.replace(".jpg", "").replace(".png", "")
    resDB = db.registerUser(nameUser, path + img)

    getEnter(screen1)

    if(resDB["affected"]):
        printShow(screen1, "¡Éxito! Se ha registrado correctamente", 1)
    else:
        printShow(screen1, "¡Error! No se ha registrado correctamente", 0)
    os.remove(img)

# Metodo que recorta la imagen o foto tomada y la recorta la
# imagen de tal manera que solo quede el rostro del usuario

def getFace(img, faces):
    data = plt.imread(img)
    for i in range(len(faces)):
        x1, y1, ancho, alto = faces[i]["box"]
        x2, y2 = x1 + ancho, y1 + alto
        plt.subplot(1, len(faces), i + 1)
        plt.axis("off")
        face = cv2.resize(data[y1 : y2, x1 : x2], (150,200), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(img, face)
        plt.imshow(data[y1 : y2, x1 : x2])

# Metodo para tomar una foto en tiempo real usando la Camara Web y OpenCV
# Se encendera la camara web para tomar una foto y asignarla a un usuario
# Este metodo pertenece al Boton Iniciar Sesion

def loginRecording():
    cap = cv2.VideoCapture(0)
    userLog = user2.get()
    img = f"{userLog}Login.jpg"
    imgUser = f"{userLog}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Inicio de Sesion", frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    userEntry2.delete(0, END)
    pixels = plt.imread(img)
    faces = MTCNN().detect_faces(pixels)

    getFace(img, faces)
    getEnter(screen2)

    # Consultar a la Base de Datos y comprobar Rostros

# Metodo que recibe dos imagenes, siendo mas especificos 2
# imagenes del Rostro de Usuario y los compara utilizando
# los Objetos Comparables y OpenCV. La comparacio nse hace
# mediante el metodo u algoritmo BFMatcher, se aceptara un
# porcentaje de similitud o compatibilidad del 95% o mas

def compatibility(img1, img2):
    orb = cv2.ORB_create()

    kpa, dac1 = orb.detectAndCompute(img1, None)
    kpa, dac2 = orb.detectAndCompute(img2, None)

    comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    matches = comp.match(dac1, dac2)

    similar = [x for x in matches if x.distance < 70]
    if len(matches) == 0:
        return 0
    return len(similar) / len(matches)

# Metodo para mostrar un mensaje segun la accion que realice el Usuario

def printShow(screen, msg, flag):
    if flag:
        print(colorSuccess + msg + colorNormal)
        screen.destroy()
        msg.showinfo(message = msg, title = "¡Éxito!")
    else:
        print(colorError + msg + colorNormal)
        Label(screen, text = msg, fg = "red", bg = colorBackground, font = (fontLabel, 12)).pack()

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
