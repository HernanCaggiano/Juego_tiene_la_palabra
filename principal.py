#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from final import *
from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        tiempo_inicio_temporizador = pygame.time.get_ticks()/1000

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras con...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        #Sonido de fondo:
        MusicaDeFondo = pygame.mixer.Sound("Sonidos/MusicaFondo.mp3")
        MusicaDeFondo.play()

        #variables
        puntos = 0
        candidata = ""
        diccionario = []
        palabrasAcertadas = []
        musicaFinal = pygame.mixer.Sound("Sonidos/GameOver.mp3")

        #incluir variables que van a servir para visualizar en la pantalla de inicio
        texto_intro = pygame.font.SysFont('console',20,True)
        texto_resultado = pygame.font.SysFont('console',50,True)
        texto_tecla = pygame.font.SysFont('console',30,True)
        esta_en_intro = True
        gana = False

        #cargo el sonido para las correctas
        correcta = pygame.mixer.Sound("Sonidos/PalabraCorrecta.mp3")
        #cargo el sonido para las incorrectas
        incorrecta = pygame.mixer.Sound("Sonidos/PalabraIncorrecta.mp3")
        #cargo el sonido para las repetidas
        repetida = pygame.mixer.Sound("Sonidos/PalabraRepetida.mp3")

        #lee el diccionario
        lectura(diccionario)

        #elige las 7 letras al azar y una de ellas como principal
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)


        #utilizacion de variables antes de que inicie el ciclo del juego
        #Seccion de intro
        while esta_en_intro:
            #evento de boton de cierre de ventana
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

            screen.fill(NEGRO)
            titulo = texto_intro.render('¡BIENVENIDO!', 1, (AMARILLO))
            reglas = texto_intro.render('REGLAS: ', 1, (AMARILLO))
            instrucciones = texto_intro.render('Se juega de a un jugador. Cada jugador cuenta con 60 segundos', 1, (ANARANJADO))
            instrucciones2 = texto_intro.render('para obtener la mayor cantidad de puntos. No se admiten', 1, (ANARANJADO))
            instrucciones3= texto_intro.render('plurales ni formas verbales conjugadas.', 1, (ANARANJADO))
            puntuacion = texto_intro.render('PUNTUACION: ', 1, (AMARILLO))
            instrucciones4 = texto_intro.render('las palabras de 3 letras dan 1 punto y las de 4 letras,',1 , ANARANJADO)
            instrucciones5 = texto_intro.render('2 puntos. A partir de 5 letras, se obtendrá tantos puntos', 1, ANARANJADO)
            instrucciones6 = texto_intro.render('como letras tenga la palabra. Los heptacracks valen 10', 1, ANARANJADO)
            instrucciones7 = texto_intro.render('puntos y cada error resta 1 punto.', 1, ANARANJADO)
            suerte = texto_resultado.render('¡¡ SUERTE !!', 1, AMARILLO)
            tecla_comenzar = texto_tecla.render('Presione ENTER para comenzar..', 1, AMARILLO)


            screen.blit(titulo,((ANCHO//2)-(titulo.get_width()//2), 30))
            screen.blit(reglas, (120, 100))
            screen.blit(instrucciones, (40, 130))
            screen.blit(instrucciones2, (40, 150))
            screen.blit(instrucciones3, (40, 170))
            screen.blit(puntuacion, (110,200))
            screen.blit(instrucciones4, (40,220))
            screen.blit(instrucciones5, (40,240))
            screen.blit(instrucciones6, (40,260))
            screen.blit(instrucciones7, (40,280))
            screen.blit(suerte, (ANCHO // 2,520))
            screen.blit(tecla_comenzar, (220,350))


            tiempo_temporizador = 0

            tiempo_actual = pygame.time.get_ticks()/1000
            tiempo_transcurrido = tiempo_actual - tiempo_inicio_temporizador

            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_RETURN]:
                esta_en_intro = False
                esta_jugando = True
            pygame.display.update()



        #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
        while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
            letrasEnPantalla = dame7Letras()
            letraPrincipal = dameLetra(letrasEnPantalla)

        print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

        #dibuja la pantalla la primera vez
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos, palabrasAcertadas)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            #pantalla de finalización
            if segundos < 1:
                MusicaDeFondo.stop()
                musicaFinal.play()
                pantallaFinal(puntos)

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():


                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:

                    letra = dameLetraApretada(e.key)
                    candidata += letra   #va concatenando las letras que escribe

                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1] #borra la ultima

                    if e.key == K_RETURN:  #presionó enter

                        #proceso = procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario,palabrasAcertadas)
                        if candidata in palabrasAcertadas or len(candidata)<3:
                            #esto es para no dar puntos repiten la candidata y que suene el sonido de incorrectas
                            proceso=0
                            repetida.play()
                        else:
                            proceso = procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario,palabrasAcertadas)
                            if proceso>0: #si la funcion proceso me trae un valor positivo distinto de 0  entonces suena el sonido de acertar
                                correcta.play()
                            else: # en caso contrario suena la de error
                                incorrecta.play()



                        puntos = puntos + proceso
                        print(palabrasAcertadas)
                        candidata = ""


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + tiempo_transcurrido

            #Limpiar pantalla anterior
            screen.fill(AMARILLO)

            #Dibujar de nuevo todo
            dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos, palabrasAcertadas)

            pygame.display.update()

            pygame.display.flip()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
