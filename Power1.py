# -*- coding: iso-8859-1 -*-

from OpenGL.GL import *
from math import *

class Power1:
    def __init__(self, x, y):
        self.x = x  # Centro cabeza eje x
        self.y = y # Centro cabeza eje y
        self.life = 1

    def dibujar(self):
        glPushMatrix()
        glPopMatrix()
