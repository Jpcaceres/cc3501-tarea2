# -*- coding: iso-8859-1 -*-

from Vector2D import *
from OpenGL.GL import *

class Pug:
    def __init__(self,):
        self.w = 30 #Ancho aprox de pug
        self.h = 50 #Alto aprox de pug

    def dibujar(self):
        glPushMatrix()
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(0.0, 0.0)
        glVertex2f(150.0, 0.0)
        glVertex2f(75.0, 100.0)
        glEnd()
        glPopMatrix()