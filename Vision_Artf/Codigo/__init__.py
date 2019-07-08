import cv2
import numpy as np
import serial

captura = cv2.VideoCapture(0);

ser = serial.Serial('COM4', 9600)

while(1):
    
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    verde_bajo = np.array([49, 50, 50], dtype=np.uint8)
    verde_alto = np.array([100, 255, 255], dtype=np.uint8)
    azul_bajo = np.array([100, 65, 75], dtype=np.uint8)
    azul_alto = np.array([130, 255, 255], dtype=np.uint8)
    rojo_bajo1 = np.array([0, 65, 75], dtype=np.uint8)
    rojo_alto1 = np.array([12, 255, 255], dtype=np.uint8)
    rojo_bajo2 = np.array([240, 65, 75], dtype=np.uint8)
    rojo_alto2 = np.array([256, 255, 255], dtype=np.uint8)
    
    mascara_verde = cv2.inRange(hsv, verde_bajo, verde_alto)
    mascara_azul = cv2.inRange(hsv, azul_bajo, azul_alto)
    mascara_roja1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
    mascara_roja2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
    
    kernel = np.ones((6, 6), np.uint8)
    
    mascara_verde = cv2.morphologyEx(mascara_verde, cv2.MORPH_CLOSE, kernel)
    mascara_verde = cv2.morphologyEx(mascara_verde, cv2.MORPH_OPEN, kernel)
    macara_azul = cv2.morphologyEx(mascara_azul, cv2.MORPH_CLOSE, kernel)
    mascara_azul = cv2.morphologyEx(mascara_azul, cv2.MORPH_OPEN, kernel)
    mascara_roja1 = cv2.morphologyEx(mascara_roja1, cv2.MORPH_CLOSE, kernel)
    mascara_roja1 = cv2.morphologyEx(mascara_roja1, cv2.MORPH_OPEN, kernel)
    mascara_roja2 = cv2.morphologyEx(mascara_roja2, cv2.MORPH_CLOSE, kernel)
    mascara_roja2 = cv2.morphologyEx(mascara_roja2, cv2.MORPH_OPEN, kernel)
    
    mask = cv2.add(mascara_verde, mascara_azul)
    mask = cv2.add(mask, mascara_roja1)
    mask = cv2.add(mask, mascara_roja2)
    
    momento = cv2.moments(mask)
    area = momento['m00']
    
    momento_v = cv2.moments(mascara_verde)
    area_v = momento_v['m00']
    
    momento_a = cv2.moments(mascara_azul)
    area_a = momento_a['m00']
    
    momento_r1 = cv2.moments(mascara_roja1)
    area_r1 = momento_r1['m00']
    
    momento_r2 = cv2.moments(mascara_roja2)
    area_r2 = momento_r2['m00']
    
    if (area_v > 1000000):
        ser.write('a')
        print('Objeto VERDE!')
        
    if (area_a > 1000000):
        ser.write('b')
        print('Objeto AZUL!')
        
    if (area_r1 > 1000000):
        ser.write('c')
        print('Objeto ROJO!')
        
    if (area_r2 > 1000000):
        ser.write('c')
        print('Objeto ROJO!')
        
    if (area > 1000000):
        print('Objeto Detectado!!')
    else:
        print('Nothing')
    
    cv2.imshow('MASCARA', mask)
    cv2.imshow('CAMARA', imagen)
    
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()
