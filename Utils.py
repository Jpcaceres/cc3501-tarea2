from random import *


def tope(pug, enemigo1, enemigo2, run):
    if abs(pug.x - enemigo1.x) < 60 and abs(pug.y - enemigo1.y) < 60:
        print('GAMER OVER (TOPE)')
        return False
    elif abs(pug.x - enemigo2.x) < 60 and abs(pug.y - enemigo2.y) < 60:
        print('GAMER OVER (TOPE)')
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


def comprobarLife(pug, run):
    if pug.life == False:
        print('GAMER OVER')
        return False
    else:
        return run


