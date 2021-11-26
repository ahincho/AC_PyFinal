
# Primer Avance - Proyecto Final de AC

# Deteccion de rostros en videos usando Python y la libreria OpenCV

# Autores:
# Hincho Jove, Angel Eduardo
# Guerra Rosas, Rodrigo Raul

import cv2
import numpy as np

# Iniciamos el video-streaming, puede ser un video grabado o en directo

cap = cv2.VideoCapture(0)

# Cargamos el clasificador de rostros frontal con ayuda de cv2

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ciclo while 'infinito' con el valor booleano true

while True:
    
    # Creamos el frame donde recibiremos la entrada por video de la camara web

    ret,frame = cap.read()

    # Cambiamos las imagenes recibidas por la camara web a escala de grises

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectamos los rostros captados por la camara web usando el clasificador frontal
    # de rostros y las imagenes enviadas en escala de grises, con una reduccion del 10%

    faces = faceClassif.detectMultiScale(gray, 1.1, 5)

    # Por cada rostro detectado, debemos encerrarlo o rodearlo de un rectangulo para
    # que sea de facil percepcion o deteccion para el usuario de nuestro sistema

    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
    
    # Mostramos en una nueva ventana o frame las imagenes captadas por la camara web

    cv2.imshow('Capturando Video ...', frame)
    
    # Para poder cerrar el ciclo while 'infinito' y dejar de compartir las imagenes
    # de la camara web (Cerrar el video-streaming) debemos presionar la tecla 'q'

    cv2.putText(frame, 'Presione la letra Q para cerrar la ventana', (10, 20), 2, 0.5, (128, 0, 255), 1, cv2.LINE_AA)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dejar de usar la camara web y cerrar las ventanas o frames generados en el proceso

cap.release()
cv2.destroyAllWindows()
