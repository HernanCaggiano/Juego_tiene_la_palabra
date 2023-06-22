from principal import *
import pygame
import sys

def pantallaFinal():
    pygame.init()
    colorLetras = (200,200,200)
    tamanio = (800, 600)

    pygame.display.set_caption("Juego Finalizado")
    pantalla = pygame.display.set_mode(tamanio)

    pantalla.fill((0,0,0)) #color del fondo



    fuente = pygame.font.Font( None, 100)
    text = fuente.render("Game Over", True, colorLetras)
    text_rect = text.get_rect(center=(400,300))
    pantalla.blit(text, text_rect)

    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #cuando apretas la X de la pantalla
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


