
# Primer Avance - Proyecto Final de Arquitectura de Computadoras

# Deteccion de rostros en imagenes usando Python y la libreria OpenCV

# Autores:
# Hincho Jove, Angel Eduardo
# Guerra Rosas, Rodrigo Raul

import cv2
import numpy as np

# Cargamos el clasificador de rostros frontal con ayuda de cv2

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargamos la imagen con la cual trabajaremos, 'oficina.jpg'

image = cv2.imread('oficina.jpg')

# Transformamos la imagen a escala de grises con ayuda de cv2

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Una vez tenemos el clasificador de rostros y la imagen cargadas
# debemos entregarle al clasificador la imagen con ayuda del metodo
# 'detectMultiScale' mandando como argumento la imagen en escala de
# grises junto con otros parametros que explicaremos a continuacion

# El 1er parametro es la imagen con la que trabajaremos

# El 2do parametro especifica en que proporcion sera reducida la
# imagen, '1.1' significa que la imagen sera reducida en un 10%

# El 3er parametro nos indica cuantos vecinos 'candidatos' debe
# tener un rectangulo o pedazo de imagen que debe tener un rostro
# para ser detectado como un 'verdadero rostro' o 'caso positivo'

# El 4to y 5to parametro especifican el tamanio minimo y maximo
# posible el cual podria ocupar un rostro dentro de nuestra imagen

faces = faceClassif.detectMultiScale(image,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30, 30),
    maxSize = (200, 200))

# Una vez hayamos encontrado todos los rostros debemos iterar en
# cada uno de estos para poder dibujar rectangulos a sus alrededores
# y de esa manera sean facilmente identificables por el usuario

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Mostramos la imagen procesada con rectangulos verdes en los rostros

cv2.imshow('Oficina', image)

# Si se presiona alguna tecla entonces se cerraran todas las ventanas

cv2.waitKey(0)
cv2.destroyAllWindows()
