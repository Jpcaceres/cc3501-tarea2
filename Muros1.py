# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *


class Muros1:
    def __init__(self, x, y):
        self.x = x  # Centro muro indestructible eje x
        self.y = y  # Centro muro indestructible eje y


    def dibujar(self):
        glPushMatrix()
        glScalef(0.5, 0.5, 1.0)
        # Bloque central
        glBegin(GL_POLYGON)
        glColor4f(102.0 / 255, 107.0 / 255, 117.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y + 50)
        glVertex2f(self.x + 50, self.y + 50)
        glVertex2f(self.x + 50, self.y - 50)
        glVertex2f(self.x - 50 , self.y - 50)
        glEnd()

        # Lado superior
        glBegin(GL_POLYGON)
        glColor4f(232.0 / 255, 239.0 / 255, 249.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y + 50)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 50, self.y + 50)
        glEnd()

        #Lado inferior
        glBegin(GL_POLYGON)
        glColor4f(47.0 / 255, 49.0 / 255, 53.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y - 50)
        glVertex2f(self.x - 60, self.y - 60)
        glVertex2f(self.x + 60, self.y - 60)
        glVertex2f(self.x + 50, self.y - 50)
        glEnd()

        #Lado Izquierdo
        glBegin(GL_POLYGON)
        glColor4f(80.0 / 255, 85.0 / 255, 91.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y + 50)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x - 60, self.y - 60)
        glVertex2f(self.x - 50, self.y - 50)
        glEnd()

        # Lado Derecho
        glBegin(GL_POLYGON)
        glColor4f(165.0 / 255, 172.0 / 255, 183.0 / 255, 1.0)
        glVertex2f(self.x + 50, self.y + 50)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 60, self.y - 60)
        glVertex2f(self.x + 50, self.y - 50)
        glEnd()

        glPopMatrix()