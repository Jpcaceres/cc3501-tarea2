# -*- coding: iso-8859-1 -*-

from OpenGL.GL import *
from math import *


class Enemigo2:  # Ovni
    def __init__(self, x, y, dx, dy):
        self.x = x  # Centro cabeza eje x
        self.y = y  # Centro cabeza eje y
        self.dx = dx
        self.dy = dy
        self.life = True

    def moverIzquierda(self, lista1, lista2):
        x1 = self.x - self.dx
        if x1 > 300 and (self.y - 480) % 600 == 0 and x1 != lista1[0]:
            self.x = x1

    def moverDerecha(self, lista1, lista2):
        x2 = self.x + self.dx
        if x2 < 3260 and (self.y - 480) % 600 == 0 and x2 != lista1[0]:
            self.x = x2

    def moverArriba(self, lista1, lista2):
        y1 = self.y + self.dy
        if y1 < 2940 and (self.x - 360) % 480 == 0 and y1 != lista1[1]:
            self.y = y1

    def moverAbajo(self, lista1, lista2):
        y2 = self.y - self.dy
        if y2 > 420 and (self.x - 360) % 480 == 0 and y2 != lista1[1]:
            self.y = y2

    def dibujar(self):
        glPushMatrix()
        glScalef(0.25, 0.2, 1.0)
        # Forma
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 255.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 150)  # Centro de la cabeza
        radio = 100
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio), self.y + sin(ang_i) * radio)
        glEnd()
        # Ojo izquierdo
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 50, self.y)  # Centro de la cabeza
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + 50 + cos(ang_i) * (radio), self.y + sin(ang_i) * radio)
        glEnd()

        # Ojo derecho
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y)  # Centro de la cabeza
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x - 50 + cos(ang_i) * (radio), self.y + sin(ang_i) * radio)
        glEnd()

        # Boca
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 60)  # Centro de la cabeza
        radio = 30
        ang = pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio), self.y - 60 + sin(-1 * ang_i) * radio)
        glEnd()

        glPopMatrix()
