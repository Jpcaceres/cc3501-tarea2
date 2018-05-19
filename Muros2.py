# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *

class Muros2:
    def __init__(self):
        self.x = 300 # Centro muro indestructible eje x
        self.y = 300 # Centro muro indestructible eje y

    def dibujar(self):
        glPushMatrix()

        # Bloque central
        glBegin(GL_POLYGON)
        glColor4f(102.0 / 255, 107.0 / 255, 117.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x + 60, self.y + 60)
        glVertex2f(self.x + 60, self.y - 60)
        glVertex2f(self.x - 60 , self.y - 60)
        glEnd()

        # Lineas Ladrillos
        glBegin(GL_LINES)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 20)
        glVertex2f(self.x + 60, self.y + 20)
        glEnd()

        glBegin(GL_LINES)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y - 20)
        glVertex2f(self.x + 60, self.y - 20)
        glEnd()

        glBegin(GL_LINES)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 20, self.y - 20)
        glVertex2f(self.x + 20, self.y - 60)
        glEnd()

        glBegin(GL_LINES)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 20, self.y + 20)
        glVertex2f(self.x - 20, self.y - 20)
        glEnd()

        # Detalles ladrillo superior
        # Lado superior
        glBegin(GL_POLYGON)
        glColor4f(232.0 / 255, 239.0 / 255, 249.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x - 55, self.y + 55)
        glVertex2f(self.x + 55, self.y + 55)
        glVertex2f(self.x + 60, self.y + 60)
        glEnd()
        # Lado Izquierdo
        glBegin(GL_POLYGON)
        glColor4f(80.0 / 255, 85.0 / 255, 91.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 60)
        glVertex2f(self.x - 55, self.y + 55)
        glVertex2f(self.x - 55, self.y + 25)
        glVertex2f(self.x - 60, self.y + 20)
        glEnd()
        #Lado Inferior
        glBegin(GL_POLYGON)
        glColor4f(47.0 / 255, 49.0 / 255, 53.0 / 255, 1.0)
        glVertex2f(self.x - 60, self.y + 20)
        glVertex2f(self.x - 55, self.y + 25)
        glVertex2f(self.x + 55, self.y + 25)
        glVertex2f(self.x + 60, self.y + 20)
        glEnd()
        # Lado Derecho
        glBegin(GL_POLYGON)
        glColor4f(165.0 / 255, 172.0 / 255, 183.0 / 255, 1.0)
        glVertex2f(self.x + 60, self.y + 20)
        glVertex2f(self.x + 55, self.y + 25)
        glVertex2f(self.x + 55, self.y + 55)
        glVertex2f(self.x + 60, self.y + 60)
        glEnd()


        glPopMatrix()