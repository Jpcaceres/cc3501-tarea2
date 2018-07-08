from random import *
from Muros2 import *
from MulExplo import *
from MulVel import *
from Puerta import *


def tope(pug, enemigo1, enemigo2, enemigo3, enemigo4, run):
    if abs(pug.x - enemigo1.x) < 60 and abs(pug.y - enemigo1.y) < 60:
        print('GAMER OVER (HAS SIDO ASESINADO)')
        return False
    if abs(pug.x - enemigo2.x) < 60 and abs(pug.y - enemigo2.y) < 60:
        print('GAMER OVER (HAS SIDO SECUESTRADO)')
        return False
    if abs(pug.x - enemigo3.x) < 60 and abs(pug.y - enemigo3.y) < 60:
        print('GAMER OVER (HAS PASADO A UNA MEJOR VIDA)')
        return False
    if abs(pug.x - enemigo4.x) < 60 and abs(pug.y - enemigo4.y) < 60:
        print('GAMER OVER (HAS MUERTO)')
        return False
    else:
        return run


def movimientoAleatorio(enemigo, lista1, lista2):
    rN = randint(0, 3)
    if rN == 0 and enemigo.life == True:
        enemigo.moverArriba(lista1, lista2)
        enemigo.dibujar()
    elif rN == 1 and enemigo.life == True:
        enemigo.moverAbajo(lista1, lista2)
        enemigo.dibujar()
    elif rN == 2 and enemigo.life == True:
        enemigo.moverIzquierda(lista1, lista2)
        enemigo.dibujar()
    elif rN == 3 and enemigo.life == True:
        enemigo.moverDerecha(lista1, lista2)
        enemigo.dibujar()


def topeBomba(bomba, personaje, m):
    if (personaje.x - 360) % 480 == 0 and (personaje.y - 480) % 600 == 0:  # Intersecciones
        if abs(bomba.x - personaje.x) < 20 + 240 * m and abs(bomba.y - personaje.y) < 60:
            personaje.life = False
        elif abs(bomba.y - personaje.y) < 150 + 300 * m and abs(bomba.x - personaje.x) < 60:
            personaje.life = False
    elif (personaje.x - 360) % 480 != 0 and (personaje.y - 480) % 600 == 0:  # pasillo vertical
        if abs(bomba.x - personaje.x) < 20 + 240 * m and abs(bomba.y - personaje.y) < 60:
            personaje.life = False
    elif (personaje.x - 360) % 480 == 0 and (personaje.y - 480) % 600 != 0:  # pasillo horizontal
        if abs(bomba.y - personaje.y) < 150 + 300 * m and abs(bomba.x - personaje.x) < 60:
            personaje.life = False

def topeMuroBomba(bomba, listaMuros, m):
    for x in listaMuros:
        if (x[0] - 60) % 240 != 0 and (x[1] - 60) % 240 != 0:  # Intersecciones
            if abs(bomba.x - x[0] * 2) < 20 + 240 * m and abs(bomba.y - x[1] * 2.5 + 30) < 60:
                listaMuros.remove(x)
            elif abs(bomba.y - x[1] * 2.5 + 30) < 150 + 300 * m and abs(bomba.x - x[0] * 2) < 60:
                listaMuros.remove(x)
        if (x[0] - 60) % 240 == 0 and (x[1] - 60) % 240 != 0:
            if abs(bomba.x - x[0] * 2) < 20 + 240 * m and (bomba.y - x[1] * 2.5 + 30) < 60:
                listaMuros.remove(x)
        elif (x[0] - 60) % 240 != 0 and (x[1] - 60) % 240 == 0:
            if (bomba.y - x[1] * 2.5 + 30) < 150 + 300 * m and abs(bomba.x - x[0] * 2) < 60:
                listaMuros.remove(x)


def comprobarLife(pug, run):
    if pug.life == False:
        print('GAMER OVER')
        return False
    else:
        return run

def comprobarLifeEnemigos(enemigo1, enemigo2, enemigo3, enemigo4):
    if enemigo1.life == False:
        enemigo1.morir()
    if enemigo2.life == False:
        enemigo2.morir()
    if enemigo3.life == False:
        enemigo3.morir()
    if enemigo4.life == False:
        enemigo4.morir()



def ponerMuros(n, posInit):
    listaMuros = []
    num = 0
    while num < n:
        i = randrange(1, 14, 1)
        j = randrange(2, 10, 1)
        if ([60 + 120 * i, 60 + 120 * j] != posInit[0]) or ([60 + 120 * i, 60 + 120 * j] != posInit[1]) or ([60 + 120 * i, 60 + 120 * j] != posInit[2]) or ([60 + 120 * i, 60 + 120 * j] != posInit[3]):
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0): # Si hay muros indestructibles
                if listaMuros.count([60 + 120 * i, 60 + 120 * j]) == 0:
                    listaMuros.append([60 + 120 * i, 60 + 120 * j])
                    num = num + 1

    return listaMuros


def vistaMuros(listaMuros):
    for x in listaMuros:
        muros2 = Muros2(x[0], x[1])
        muros2.dibujar()

def ponerMul(listaMuros):
    m1 = [listaMuros[0][0], listaMuros[0][1]]
    m2 = [listaMuros[1][0], listaMuros[1][1]]
    m3 = [listaMuros[2][0], listaMuros[2][1]]
    listaMul = [m1, m2, m3]
    return listaMul


def topeMulExplo(pug, MulExplo, m):
    if abs(pug.x - MulExplo.x * 2) < 60 and abs(pug.y - MulExplo.y * 2.5 - 30) < 60:
        MulExplo.life = False
        return 2
    return m

def topeMulVel(pug, MulVel):
    if abs(pug.x - MulVel.x * 2) < 60 and abs(pug.y - MulVel.y * 2.5 - 30) < 60:
        MulVel.life = False
        pug.dx = 240
        pug.dy = 300
        return 0
    return 1

def topePuerta(pug, Puerta):
    if abs(pug.x - Puerta.x * 2) < 60 and abs(pug.y - Puerta.y * 2.5 - 30) < 60:
        pug.life = False
        print("FELICITACIONES HAS GANADO")
        return 0
    return 1







