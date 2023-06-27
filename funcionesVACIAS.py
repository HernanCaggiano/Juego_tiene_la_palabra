from principal import *
from configuracion import *
import random
import math


#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    archivo = open("lemario.txt", "r", encoding = "latin-1")
    for linea in archivo.readlines():
        diccionario.append(linea[0:-1])
    archivo.close()
    return diccionario


def dame7Letras():
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w"]
    consonatesDificiles = ["k", "x", "y", "z"]
    cadena = []

    #agrega 2 o 3 vocales a la cadena
    numVocales = random.randint(2, 3) #genera un numero aleatorio entre 2 o 3
    vocal = random.sample(vocales, numVocales) #selecciona 2 o 3 vocales sin repetir
    cadena.extend(vocal)

    #agrega una consonante dificil
    if random.random() < 0.5:
        consonante = random.choice(consonatesDificiles)#selecciona una consonante con 50% de probabilidad
        cadena.append(consonante)


    #completa con letras aleatorias
    while len(cadena) < 7:
        caracter = random.choice(consonantes)
        if not(caracter in cadena):
            cadena.append(caracter)

    random.shuffle(cadena) #mezcla las letras de forma aleatoria

    letras = "".join(cadena)

    return letras


def dameLetra(letrasEnPantalla):
    letraPrincipal = random.choice(letrasEnPantalla)
    return letraPrincipal


#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas):
    valida = esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas)

    if valida:
        return Puntos(candidata)
    else:
        return -1


#nueva funcion: limitar palabras a letras en pantalla
def soloLetrasPantalla(candidata, letrasEnPantalla): #AGREGADA
    for i in candidata:
        if not(i in letrasEnPantalla):
            return False
    return True


#nueva funcion:
def existeEnDiccionario(candidata, diccionario): #AGREGADA

    if candidata in diccionario:
        return True
    else:
        return False


#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, palabrasAcertadas):

    letras = soloLetrasPantalla(candidata, letrasEnPantalla)
    enDiccionario = existeEnDiccionario(candidata, diccionario)

    if letraPrincipal in candidata:
        if letras and enDiccionario:
            palabrasAcertadas.append(candidata)
            return True
        else:
            return False
    else:
        return False


#devuelve los puntos
def Puntos(candidata):
    longitud = len(candidata)

    if longitud == 3:
        puntos = 1
    elif longitud == 4:
        puntos = 2
    elif longitud == 7:
        puntos = 10
    else:
        puntos = longitud
    return puntos



#busca en el diccionario palabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    correctas = []

    for palabra in diccionario:
        #Chequeo si la letra principal está en la palabra del diccionario
        if letraPrincipal in palabra and len(palabra) > 2:
            cumple = True
            #Chequeo si las letras de la palabra están en las letras en pantalla
            for char in palabra:
                if char not in letrasEnPantalla:
                    cumple = False
            if cumple:
                correctas.append(palabra)
    return correctas