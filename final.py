from principal import *
from configuracion import *
import pygame
import sys

def pantallaFinal(puntos):
    pygame.init()
    colorLetras = (200,200,200)
    tamanio = (800, 600)

    pygame.display.set_caption("Juego Finalizado")
    pantalla = pygame.display.set_mode(tamanio)

    pantalla.fill(AMARILLO) #color del fondo

    pygame.draw.rect(pantalla, ANARANJADO, (200, 200, 400, 100))

    pygame.draw.rect(pantalla, ANARANJADO, (310, 440, 240, 40))

    pygame.draw.rect(pantalla, ANARANJADO, (85, 540, 500, 40))



    fuente = pygame.font.Font( None, 100)
    texto_intro = pygame.font.SysFont('console',20,True)

    text = fuente.render("Game Over", True, colorLetras)
    text_rect = text.get_rect(center=(400,250))
    puntaje = texto_intro.render('Puntaje Final :' + str(puntos), 1, colorLetras)
    mensaje = texto_intro.render('Presione Escape para cerrar la ventana.', 1, colorLetras)
    pantalla.blit(text, text_rect)
    pantalla.blit(puntaje, (330,450))
    pantalla.blit(mensaje, (100,550))
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


