#!/usr/bin/env python
# coding: utf-8

# <figure>
# <img src="../Imagenes/logo-final-ap.png"  width="80" height="80" align="left"/> 
# </figure>
# 
# # <span style="color:blue"><left>Aprendizaje Profundo</left></span>

# # <span style="color:red"><center>Visión por Computadora</center></span>
# ## <span style="color:red"><center>Ejemplos de proyectos</center></span>

# ## <span style="color:blue">Contenido</span>

# * [Paquetes a usar](#Paquetes-a-usar)
# * [Detección de códigos QR](#Detección-de-códigos-QR)
# * [Detección facial básica](#Detección-facial-básica)

# ## <span style="color:blue">Paquetes a usar</span>

# In[1]:


import cv2
import webbrowser
import os


# ## <span style="color:blue">Detección de códigos QR</span>
# 
# Vamos a usar la cámara web para reconocer códigos QR y entrar a los enlaces de estos

# In[2]:


## Iniciamos la cámara
cap = cv2.VideoCapture(0)
# Llamamos el detector de QR
detector = cv2.QRCodeDetector()

# en este loop va a leer la cámara web y generará una variable vacía donde se guarda la imágen
while True:
    _, img = cap.read()

# detección y decodificación del QR
    data, points, _ = detector.detectAndDecode(img)
   # Busca si hay un QR en la cámara y paramos el loop si hay un QR
    if data:
        a = data
        break


# se muestra el output de la cámara web
    cv2.imshow("QRCODEscanner", img)
# si se usa la tecla "q", se parará el loop
    if cv2.waitKey(1) == ord("q"):
        break

# obtenemos el url en el QR y lo abrimos
b=webbrowser.open(str(a))
#cerramos la camara y cerramos todas las ventanas que hemos abierto
cap.release()
cv2.destroyAllWindows()


# ## <span style="color:blue">Detección facial básica</span>
# 
# Vamos a usar la cámara web para encontrar rostros y generar un cuadro en este

# In[4]:


# Llamamos el modelo pre entrenado de clasificadores con cascada de haar
cascPath='../modelos/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(cascPath)

# Iniciamos la cámara
cap = cv2.VideoCapture(0)

while True:
    # Hacemos la captura fotograma por fotograma
    ret, frames = cap.read()
    #cambiamos a escala de grises
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    #iniciamos el modelo de detección
    faces = faceCascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    # Dibujamos el rectángulo 
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # mostramos el fotograma final
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) == ord('q'):
        break

#cerramos la camara y cerramos todas las ventanas que hemos abierto
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" property="dct:title" rel="dct:type">pruebas sphinx</span> por <a xmlns:cc="http://creativecommons.org/ns#" href="https://aprendizajeprofundo.co" property="cc:attributionName" rel="cc:attributionURL">aprendizaje profundo</a> se distribuye bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional</a>.
