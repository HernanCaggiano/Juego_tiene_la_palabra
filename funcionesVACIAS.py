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


    letras = "".join(cadena) #transforma la lista en un string

    return letras




#elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla):
    letraPrincipal = random.choice(letrasEnPantalla)
    return letraPrincipal



#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    valida = esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario)
    correcta = pygame.mixer.Sound("Sonidos/PalabraCorrecta.mp3")
    incorrecta = pygame.mixer.Sound("Sonidos/PalabraIncorrecta.mp3")

    if valida:
        correcta.play()
        return Puntos(candidata)
    else:
        incorrecta.play()
        return -1




#limitar palabras a letras en pantalla
def soloLetrasPantalla(candidata, letrasEnPantalla): #AGREGADA
    for i in candidata:
        if not(i in letrasEnPantalla):
            return False
    return True




#funcion de si existe en el diccionario
def existeEnDiccionario(candidata, diccionario): #AGREGADA

    if candidata in lectura(diccionario):
        return True
    else:
        return False



#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):

    letras = soloLetrasPantalla(candidata, letrasEnPantalla)
    enDiccionario = existeEnDiccionario(candidata, diccionario)
    print(letras)
    print(enDiccionario)

    if letraPrincipal in candidata:
        if letras and enDiccionario:
            return True
        else:
            return False
    else:
        return False




#devuelve los puntos
def Puntos(candidata):

    longitud = len(candidata)
    #devuelve los puntos de acuerdo a la cantidad de letras
    if longitud < 3:
        return -1
    elif longitud == 3:
        return 1
    elif longitud == 4:
        return 2
    elif longitud >= 5:
        if longitud == 7:
            return 10
        else:
            return longitud





#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    palabrasAcertadas = []
    diccionario = lectura(diccionario)



    for palabra in diccionario:                                           #Se utiliza el ciclo for para iterar por cada palabra
        cumple = True                                                     #Se declara la variable "cumple" como True
        for letra in palabra:                                             #Dentro se usa otro ciclo for para iterar por cada letra de la palabra
            if not(letra in letrasEnPantalla or letra in letraPrincipal): #Se verifica si cada letra de la palabra esta presente en la pantalla
                cumple = False                                            #Si alguna no cumple se establece la variable "cumple" como False
                break                                                     #Y se rompe el ciclo interno
        if cumple:                                                        #Se verifica si la variable "cumple" es True, Si es True significa que todas las letras de la palabra estan en la pantalla
            palabrasAcertadas.append(palabra)                             #Agrega la palabra a la lista "palabrasAcertadas"

    return palabrasAcertadas



    #return ['adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']
