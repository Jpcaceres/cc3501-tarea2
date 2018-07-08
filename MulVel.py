# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *
from math import *


class MulVel:
    def __init__(self, x, y, life):
        self.x = x  # Centro muro indestructible eje x
        self.y = y  # Centro muro indestructible eje y
        self.life = life

    def dibujar(self):
        glPushMatrix()
        glScalef(0.5, 0.5, 1.0)
        #Contorno
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 255.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 60, self.y - 60)
        glVertex2f(self.x - 60, self.y - 60)
        glEnd()
        # Bloque central
        glBegin(GL_POLYGON)
        glColor4f(219.0 / 255, 196.0 / 255, 24.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y + 50)
        glVertex2f(self.x + 50, self.y + 50)
        glVertex2f(self.x + 50, self.y - 50)
        glVertex2f(self.x - 50, self.y - 50)
        glEnd()
        # Icono de velocidad
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(255.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 40, self.y)  # Centro de la cabeza
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + 10 + cos(ang_i) * radio, self.y + sin(ang_i) * radio)
        glEnd()


        glPopMatrix()
