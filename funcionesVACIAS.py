from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    archivo = open("lemario.txt", "r", encoding = "ISO-8859-1")
    leerArc = archivo.readlines()
    diccionario = []
    nuevoDiccionario = []

#ciclo que recorre el archivo y lo agrega a una lista
    for i in leerArc:
        diccionario.append(i)
    archivo.close()

#ciclo que quita el ultimo caracter de cada elemento de la lista
    for i in range(len(diccionario)):
        elemt = diccionario[i][:-1]
        nuevoDiccionario.append(elemt)

    return nuevoDiccionario
    #return ['programacion', 'ungs', 'universidad', 'juego', 'palabras', 'laboratorio', 'cadenas', 'adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']



#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w"]
    consonatesDificiles = ["k", "x", "y", "z"]
    cadena = ""

    #agrega 2 o 3 vocales a la cadena
    numVocales = random.randint(2, 3)
    cadena = random.choices(vocales, k=numVocales)

    #agrega una consonante dificil
    if random.random() < 0.5:
        consonante = random.choice(consonatesDificiles)
        cadena.append(consonante)

    #completa con letras aleatorias
    while len(cadena) < 7:
        caracter = random.choice(consonantes)
        if not(caracter in cadena):
            cadena.append(caracter)

    random.shuffle(cadena) #mezcla las letras de forma aleatoria

    return "".join(cadena)




def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
    letraPrincipal = random.choice(letrasEnPantalla)
    return letraPrincipal



#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    return Puntos(candidata)



#AGREGADAS:
#funcion chequea que solo use las letras de la pantalla
def palabraArmada(candidata, letrasEnPantalla):
    for i in candidata:
        if i in letrasEnPantalla:
            continue
        else:
            return False
    return True

#funcion de si existe en el diccionario
def existeEnDiccionario(candidata, diccionario):
    if candidata in diccionario:
        return True
    else:
        return False
#################

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):

    letras = palabraArmada(candidata, letrasEnPantalla)
    enDiccionario = existeEnDiccionario(candidata, diccionario)

    if (letraPrincipal in candidata) and letras and enDiccionario:
        return True
    else:
        return False
    #return True




#devuelve los puntos
def Puntos(candidata):

    longitud = len(candidata)
    #devuelve los puntos de acuerdo a la cantidad de letras
    if longitud == 3:
        return 1
    elif longitud == 4:
        return 2
    elif longitud >= 5:
        if longitud == 7:
            return 10
        else:
            return longitud
    #return(5)




#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabrasAcertadas = []
    diccionario = lectura(diccionario)

    for palabra in diccionario:
        cont = 0
        for letra in letrasEnPantalla:
            if letra in palabra:
                cont += 1
            if cont == 7:
                palabrasAcertadas.append(palabra)

    return palabrasAcertadas

    #return ['adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']
