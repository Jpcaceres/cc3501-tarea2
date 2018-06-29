# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *
from Bombas import *


class MulExplo:
    def __init__(self, x, y):
        self.x = 180  # Centro muro indestructible eje x
        self.y = 180  # Centro muro indestructible eje y

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
        glColor4f(255.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 50, self.y + 50)
        glVertex2f(self.x + 50, self.y + 50)
        glVertex2f(self.x + 50, self.y - 50)
        glVertex2f(self.x - 50, self.y - 50)
        glEnd()
        bomba = Bombas()
        bomba.transladar(180 * 4,180 * 5)
        bomba.dibujar()


        glPopMatrix()
