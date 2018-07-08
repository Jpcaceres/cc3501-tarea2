# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *


class Puerta:
    def __init__(self, x, y):
        self.x = x  # Centro muro indestructible eje x
        self.y = y  # Centro muro indestructible eje y


    def dibujar(self):
        glPushMatrix()
        glScalef(0.5, 0.5, 1.0)
        # Bloque central
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 60, self.y - 60)
        glVertex2f(self.x - 60, self.y - 60)
        glEnd()

        #Madera Izquierda
        glBegin(GL_POLYGON)
        glColor4f(114.0 / 255, 68.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x - 5, self.y + 60)
        glVertex2f(self.x - 5, self.y - 60)
        glVertex2f(self.x - 60, self.y - 60)
        glEnd()

        # Madera Derecha
        glBegin(GL_POLYGON)
        glColor4f(114.0 / 255, 68.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 5, self.y + 60)
        glVertex2f(self.x + 5, self.y - 60)
        glVertex2f(self.x + 60, self.y - 60)
        glEnd()

        # Perilla Izquierda
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 10, self.y + 5)
        glVertex2f(self.x - 20, self.y + 5)
        glVertex2f(self.x - 20, self.y - 5)
        glVertex2f(self.x - 10, self.y - 5)
        glEnd()

        # Perilla Derecha
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 10, self.y + 5)
        glVertex2f(self.x + 20, self.y + 5)
        glVertex2f(self.x + 20, self.y - 5)
        glVertex2f(self.x + 10, self.y - 5)
        glEnd()





        glPopMatrix()

