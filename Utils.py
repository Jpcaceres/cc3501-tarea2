from math import *


def tope(pug, enemigo1, enemigo2, run):
    if abs(pug.x - enemigo1.x) < 60 and abs(pug.y - enemigo1.y) < 60:
        print('GAMER OVER')
        return False
    elif abs(pug.x - enemigo2.x) < 60 and abs(pug.y - enemigo2.y) < 60:
        print('GAMER OVER')
        return False
    else:
        return run

def topeBomba(bomba, pug, enemigo1, enemigo2, m, run):
    if abs(bomba.x - pug.x) < 20 + 240 * m  and abs(bomba.y - pug.y) < 60:
        print('GAMER OVER')
        pug.life = False
    elif abs(bomba.y - pug.y) < 150 + 300 * m and abs(bomba.x - pug.x) < 60:
        print('GAMER OVER')
        pug.life = False
    elif abs(bomba.x - enemigo1.x) < 20 + 240 * m and abs(bomba.y - enemigo1.y) < 60:
        enemigo1.life = False
    elif abs(bomba.y - enemigo1.y) < 150 + 300 * m and abs(bomba.x - enemigo1.x) < 60:
        enemigo1.life = False
    elif abs(bomba.x - enemigo2.x) < 20 + 240 * m and abs(bomba.y - enemigo2.y) < 60:
        enemigo2.life = False
    elif abs(bomba.y - enemigo2.y) < 150 + 300 * m and abs(bomba.x - enemigo2.x) < 60:
        enemigo2.life = False

def comprobarLife(pug, run):
    if pug.life == False:
        print('GAMER OVER')
        return False
    else:
        return run


