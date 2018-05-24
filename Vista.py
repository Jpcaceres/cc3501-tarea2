# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *
from random import *
from Muros1 import *

class Vista:
    def dibujar(self, pug):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Creacion de escena
        for i in range(15):
                for j in range(11):
                    if i % 2 == 0 and j % 2 == 0:
                        murosInterior = Muros1(60 + 120 * i, 60 + 120 *j)
                        murosInterior.dibujar()
                    else:
                        if i == 0 or i == 14 or j == 0 or j == 10:
                            murosInterior = Muros1(60 + 120 * i, 60 + 120 * j)
                            murosInterior.dibujar()

        # dibuja pug
        pug.dibujar()

        glLoadIdentity()

    def poner(self, pug, bomba):
        bomba.transladar(pug.x, pug.y)
        bomba.dibujar()

    def movimientoAleatorio(self, enemigo, lista1, lista2):
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





    def explotar(self, x, y, bomba, m):
        bomba.transladar(x, y + 30)
        if x == 360 and y == 480: # esquina inf izq
            bomba.explotar(m, 0, 0, m)
        elif x == 360 and y == 2880: # esquina sup izq
            bomba.explotar(0, m, 0, m)
        elif x == 3240 and y == 480: # esquina inf der
            bomba.explotar(m, 0, m, 0)
        elif x == 3240 and y == 2880: # esquina sup der
            bomba.explotar(0, m, m, 0)
        elif (x - 360) % 480 == 0 and y == 480: # inferior
            bomba.explotar(m, 0, m, m)
        elif x == 360 and (y - 480) % 600 == 0: # izquierda
            bomba.explotar(m, m, 0, m)
        elif (x - 360) % 480 == 0 and y == 2880: # arriba
            bomba.explotar(0, m, m ,m)
        elif x == 3240 and (y - 480) % 600 == 0: # derecha
            bomba.explotar(m, m, m, 0)
        elif (y - 480) % 600 != 0:
            bomba.explotar(m, m, 0, 0)
        elif (x - 360) % 480 != 0:
            bomba.explotar(0, 0, m, m)
        else:
            bomba.explotar(m, m, m, m)






