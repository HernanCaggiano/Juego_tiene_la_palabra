# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_n and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos, palabrasAcertadas):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

    #Rectángulo de letras en pantalla
    pygame.draw.rect(screen, ANARANJADO, (120, 80, 560, 135))

    #Rectángulo de candidata
    pygame.draw.rect(screen, VERDE, (0, 520, 800, 80))

    #Rectángulo de Aciertos
    pygame.draw.rect(screen, ANARANJADO, (645, 220, 120, 300))

    ren1 = defaultFont.render(candidata, 1, ANARANJADO_OSCURO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, NEGRO)

    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, ROJO)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, NEGRO)

    ren4 = defaultFont.render("Aciertos: " + str(len(palabrasAcertadas)), 1, NEGRO)

    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 130
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, ROJO), (pos, 100))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, GRIS), (pos, 100))
        pos = pos + TAMANNO_LETRA_GRANDE

    #escribe las palabras correctas ingresadas
    pos = 250
    for c in range(len(palabrasAcertadas)):
        screen.blit(defaultFont.render(palabrasAcertadas[c], 1, NEGRO), (650, pos))
        pos = pos + 20

    screen.blit(ren1, (300, 550))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))
    screen.blit(ren4, (650, 230))