
# Primer Avance - Proyecto Final de AC

# Compatibilidad de rostros usando Python y la libreria OpenCV

# Autores:
# Hincho Jove, Angel Eduardo
# Guerra Rosas, Rodrigo Raul

import cv2
import numpy as np

# Metodo 'compatibility' recibe dos imagenes como argumentos
# para compararlas usando el metodo BFMatcher de OpenCV

# OJO: Por ahora tomaremos un porcentaje de mas del 80% de
# compatibilidad para un Caso Positivo porque aun no hemos
# implementado una Base de Datos de nuestros Usuarios

def getFace(image):

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = faceClassif.detectMultiScale(image,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (50, 50),
        maxSize = (550, 550))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)

    return image


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

# Metodo 'giveAnswer' recibe el porcentaje de compatibilidad
# entre dos imagenes y da una respuesta acorde al porcentaje

def giveAnswer(percentage):

    # Si es mayor de 80% se trata de la misma persona, en
    # caso contrario se tratan de dos personas diferentes

    print(percentage)

    if(percentage > 0.80):
        print("Las fotos pertenecen a la misma persona ...")
        cv2.imshow('Respuesta', cv2.imread('imgs/caso_positivo.png'))
    else:
        print("Las fotos pertenecen a personas diferentes ...")
        cv2.imshow('Respuesta', cv2.imread('imgs/caso_negativo.png'))

# El programa comienza abriendo dos imagenes de la carpeta 'imgs'

# Abrimos las dos imagenes a comparar y las cambiamos a escala de grises

# Caso Positivo, comparando dos imagenes de Angel ...

img1 = cv2.imread('imgs/foto_angel01.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('imgs/foto_angel02.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Caso Negativo, comparando dos imagenes de Angel y Rodrigo ...

# img1 = cv2.imread('imgs/foto_angel02.jpg')
# img2 = cv2.imread('imgs/foto_rodrigo01.jpg')

# Mostramos un recuadro alrededor de los rostros detectados

cv2.imshow("Primer Rostro ...", img1)
cv2.imshow("Segundo Rostro ...", img2)

# Verificamos la compatibilidad y damos un respuesta acorde

giveAnswer(compatibility(img1, img2))

# Presionar la tecla 'Esc' o Escape para cerrar las ventanas

cv2.waitKey(0)
cv2.destroyAllWindows()
