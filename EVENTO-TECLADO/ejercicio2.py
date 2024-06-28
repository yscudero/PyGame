#se mueve mientras la tecla está presionada
import pygame
from constantes import *
#iniciar la pantalla
pygame.init()
#POSICIONES
posicion_circulo = POSICION_CIRCULO
#crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#Seteo un título en la pantalla
pygame.display.set_caption("Juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
    #salgo del for para ver que teclas están presionadas, se lee todo el tiempo
    #funciona mientras las teclas están presionadas
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        #print(lista_teclas)
        #derecha = pygame.K_RIGHT
        #print("derecha ", derecha)
        #izquierda = pygame.K_LEFT
        #print("izquierda ", izquierda)        
        if lista_teclas[pygame.K_RIGHT]:
            posicion_circulo[0] = posicion_circulo[0] + 0.05 #se mueve 0.05 pixel #mientras #la tecla está presionada
        if lista_teclas[pygame.K_LEFT]:
            posicion_circulo[0] = posicion_circulo[0] - 0.05
        if lista_teclas[pygame.K_UP]:
            posicion_circulo[1] = posicion_circulo[1] - 0.05
        if lista_teclas[pygame.K_DOWN]:
            posicion_circulo[1] = posicion_circulo[1] + 0.05
    #fondo color
    pantalla.fill(COLOR_CELESTE)
    pygame.draw.circle(pantalla, COLOR_AMARILLO,posicion_circulo,80)
    #mostrar
    pygame.display.flip()
pygame.quit()
