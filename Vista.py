# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *
from Muros1 import *

class Vista:
    def dibujar(self,pug):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #Creacion de escena
        muros1 = Muros1()

        # dibuja la tierra
        pug.dibujar()

        glLoadIdentity()



