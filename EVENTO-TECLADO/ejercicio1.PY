#1 MOVIMIENTO POR TECLA QUE PRESIONO
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
        if evento.type == pygame.KEYDOWN: #si presionó una tecla 1vez
           if evento.key == pygame.K_RIGHT:
               posicion_circulo[0] = posicion_circulo[0]+10
           if evento.key == pygame.K_LEFT:
               posicion_circulo[0] = posicion_circulo[0]-10
           if evento.key == pygame.K_UP:
               posicion_circulo[1] = posicion_circulo[1]-10
           if evento.key == pygame.K_DOWN:
               posicion_circulo[1] = posicion_circulo[1]+10
            
    #fondo color
    pantalla.fill(COLOR_CELESTE)
    pygame.draw.circle(pantalla, COLOR_AMARILLO,posicion_circulo,80)
    #mostrar
    pygame.display.flip()
pygame.quit()
