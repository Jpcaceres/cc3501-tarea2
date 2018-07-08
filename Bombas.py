# -*- coding: iso-8859-1 -*-
from OpenGL.GL import *
from math import *

class Bombas:
    def __init__(self):
        self.x = -3000 # Centro Bomba
        self.y = -3000 # Centro Bomba

    def transladar(self, x, y):
        self.x = x
        self.y = y - 60

    def explotar(self, arriba, abajo, izquierda, derecha):
        glPushMatrix()
        glScalef(0.25, 0.2, 1.0)
        glBegin(GL_POLYGON)
        glColor4f(242.0 / 255, 70.0 / 255, 36.0 / 255, 1.0)
        glVertex2f(self.x - 120, self.y + 150 + 300 * arriba)
        glVertex2f(self.x + 120, self.y + 150 + 300 * arriba)
        glVertex2f(self.x + 120, self.y - 150 - 300 * abajo)
        glVertex2f(self.x - 120, self.y - 150 - 300 * abajo)
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(242.0 / 255, 70.0 / 255, 36.0 / 255, 1.0)
        glVertex2f(self.x + 120 + 240 * derecha, self.y - 150)
        glVertex2f(self.x + 120 + 240 * derecha, self.y + 150)
        glVertex2f(self.x - 120 - 240 * izquierda, self.y + 150)
        glVertex2f(self.x - 120 - 240 * izquierda, self.y - 150)
        glEnd()
        glPopMatrix()


    def dibujar(self):
        glPushMatrix()
        glScalef(0.25, 0.2, 1.0)
        # Forma
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y)  # Centro de la cabeza
        radio = 100
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio), self.y + sin(ang_i) * radio)
        glEnd()

        # Iluminación
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(191.0 / 255, 192.0 / 255, 193.0 / 255, 1.0)
        glVertex2f(self.x - 40, self.y)  # Centro de la iluminación
        radio = 50
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x - 40 + cos(ang_i) * (radio - 10), self.y + sin(ang_i) * (radio + 15))
        glEnd()

        # Cuadrado
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 30, self.y + 80)
        glVertex2f(self.x - 30, self.y + 80)
        glVertex2f(self.x - 30, self.y + 130)
        glVertex2f(self.x + 30, self.y + 130)
        glEnd()

        # Cuadrado Iluminacion
        glBegin(GL_POLYGON)
        glColor4f(191.0 / 255, 192.0 / 255, 193.0 / 255, 1.0)
        glVertex2f(self.x - 5, self.y + 100)
        glVertex2f(self.x - 25, self.y + 100)
        glVertex2f(self.x - 25, self.y + 125)
        glVertex2f(self.x - 5, self.y + 125)
        glEnd()

        # Cordel mecha
        glBegin(GL_POLYGON)
        glColor4f(86.0 / 255, 54.0 / 255, 22.0 / 255, 1.0)
        glVertex2f(self.x + 5, self.y + 130)
        glVertex2f(self.x - 5, self.y + 130)
        glVertex2f(self.x - 5, self.y + 180)
        glVertex2f(self.x + 5, self.y + 180)
        glEnd()

        # Fuego mecha
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(247.0 / 255, 46.0 / 255, 46.0 / 255, 1.0)
        glVertex2f(self.x, self.y + 190)  # Centro de la cabeza
        radio = 10
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio), self.y + 170 + sin(ang_i) * radio)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor4f(239.0 / 255, 170.0 / 255, 59.0 / 255, 1.0)
        glVertex2f(self.x, self.y + 185)  # Centro de la cabeza
        radio = 5
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio), self.y + 167 + sin(ang_i) * radio)
        glEnd()




        glPopMatrix()