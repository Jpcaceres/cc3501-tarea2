# -*- coding: iso-8859-1 -*-

from Vector2D import *
from OpenGL.GL import *
from math import *

class Pug:
    def __init__(self):
        self.x = 300 # Centro cabeza eje x
        self.y = 300 # Centro cabeza eje y
        self.sprite = 1
    def dibujar(self):
        glPushMatrix()

        # Torso
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 90)
        glVertex2f(self.x + 30, self.y - 90)
        glVertex2f(self.x + 30, self.y - 150)
        glVertex2f(self.x - 30 , self.y - 150)
        glVertex2f(self.x - 30, self.y - 90)
        glEnd()

        #Calavera
        glBegin(GL_POLYGON)
        glColor4f(255.0 / 255, 255.0 / 255, 255.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 105)
        glVertex2f(self.x + 20, self.y - 105)
        glVertex2f(self.x + 20, self.y - 130)
        glVertex2f(self.x + 15, self.y - 130)
        glVertex2f(self.x + 15, self.y - 140)
        glVertex2f(self.x - 15, self.y - 140)
        glVertex2f(self.x - 15, self.y - 130)
        glVertex2f(self.x - 20, self.y - 130)
        glVertex2f(self.x - 20, self.y - 105)
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 5, self.y - 115)
        glVertex2f(self.x + 15, self.y - 115)
        glVertex2f(self.x + 15, self.y - 125)
        glVertex2f(self.x + 5, self.y - 125)
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 5, self.y - 115)
        glVertex2f(self.x - 15, self.y - 115)
        glVertex2f(self.x - 15, self.y - 125)
        glVertex2f(self.x - 5, self.y - 125)
        glEnd()

        if (self.sprite == 1): #Extremidades 1
            # Brazo Izquierdo
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x - 30, self.y - 100)
            glVertex2f(self.x - 60, self.y - 100)
            glVertex2f(self.x - 60, self.y - 120)
            glVertex2f(self.x - 30, self.y - 120)
            glEnd()
            # Brazo Derecho
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x + 30, self.y - 100)
            glVertex2f(self.x + 60, self.y - 115)
            glVertex2f(self.x + 60, self.y - 135)
            glVertex2f(self.x + 30, self.y - 120)
            glEnd()
            # Pierna Derecha
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x + 30, self.y - 150)
            glVertex2f(self.x + 30, self.y - 180)
            glVertex2f(self.x + 10, self.y - 180)
            glVertex2f(self.x + 10, self.y - 150)
            glEnd()
            # Pierna Izquierda
            glBegin(GL_POLYGON)
            glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
            glVertex2f(self.x - 30, self.y - 150)
            glVertex2f(self.x - 30, self.y - 165)
            glVertex2f(self.x - 10, self.y - 165)
            glVertex2f(self.x - 10, self.y - 150)
            glEnd()

        else: #Extremidades 2
            # Brazo Izquierdo
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x - 30, self.y - 100)
            glVertex2f(self.x - 60, self.y - 115)
            glVertex2f(self.x - 60, self.y - 135)
            glVertex2f(self.x - 30, self.y - 120)
            glEnd()
            # Brazo Derecho
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x + 30, self.y - 100)
            glVertex2f(self.x + 60, self.y - 100)
            glVertex2f(self.x + 60, self.y - 120)
            glVertex2f(self.x + 30, self.y - 120)
            glEnd()
            # Pierna Derecha
            glBegin(GL_POLYGON)
            glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
            glVertex2f(self.x + 30, self.y - 150)
            glVertex2f(self.x + 30, self.y - 165)
            glVertex2f(self.x + 10, self.y - 165)
            glVertex2f(self.x + 10, self.y - 150)
            glEnd()
            # Pierna Izquierda
            glBegin(GL_POLYGON)
            glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
            glVertex2f(self.x - 30, self.y - 150)
            glVertex2f(self.x - 30, self.y - 180)
            glVertex2f(self.x - 10, self.y - 180)
            glVertex2f(self.x - 10, self.y - 150)
            glEnd()

        # Cabeza (Forma)
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(232.0 / 255, 172.0 / 255, 69.0 / 255, 1.0)
        glVertex2f(self.x , self.y) #Centro de la cabeza
        radio = 100
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio + 15), self.y + sin(ang_i) * radio)
        glEnd()

        # Hocico (Forma)
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 50)  # Centro de la cabeza
        radio = 60
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio + 15), (self.y - 40) + sin(ang_i) * radio)
        glEnd()

        # Mancha Ojo Izquierdo
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
        glVertex2f(self.x - 70 , self.y + 10)
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x - 70) + cos(ang_i) * radio, (self.y + 10) +sin(ang_i) * radio)
        glEnd()

        # Ojo Izquierdo
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(255.0 / 255, 255.0 / 255, 255.0 / 255, 1.0)
        glVertex2f(self.x - 70, self.y + 10)
        radio = 20
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x - 70) + cos(ang_i) * radio, (self.y + 10) + sin(ang_i) * radio)
        glEnd()

        # Lobulo Ojo Izquierdo
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x - 75, self.y + 10)
        radio = 15
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x - 75) + cos(ang_i) * radio, (self.y + 10) + sin(ang_i) * radio)
        glEnd()

        # Mancha Ojo Derecho
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
        glVertex2f(self.x + 70, self.y + 10)
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x + 70) + cos(ang_i) * radio, (self.y + 10) + sin(ang_i) * radio)
        glEnd()

        # Ojo Derecho
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(255.0 / 255, 255.0 / 255, 255.0 / 255, 1.0)
        glVertex2f(self.x + 70, self.y + 10)
        radio = 20
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x + 70) + cos(ang_i) * radio, (self.y + 10) + sin(ang_i) * radio)
        glEnd()

        # Lobulo Ojo Derecho
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x + 75, self.y + 10)
        radio = 15
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex((self.x + 75) + cos(ang_i) * radio, (self.y + 10) + sin(ang_i) * radio)
        glEnd()

        # Nariz
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 25)  # Centro de la cabeza
        radio = 15
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * (radio + 10), (self.y + 5) + sin(ang_i) * radio)
        glEnd()

        # Lengua
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(244.0 / 255, 88.0 / 255, 88.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 45)  # Centro de la lengua
        radio = 25
        ang = pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i) * radio, (self.y - 45) + sin(-1 * ang_i) * (radio + 10))
        glVertex2f(self.x, self.y - 45)
        glEnd()

        # Boca
        glBegin(GL_LINES)
        glColor4f(0.0 / 255, 0.0 / 255, 0.0 / 255, 1.0)
        glVertex2f(self.x, self.y - 25)  # Centro de la cabeza
        glVertex2f(self.x, self.y - 45)
        glVertex2f(self.x - 40, self.y - 45)
        glVertex2f(self.x + 40, self.y - 45)
        glEnd()

        # Pelo
        glBegin(GL_TRIANGLE_FAN)
        glColor4f(68.0 / 255, 51.0 / 255, 22.0 / 255, 1.0)
        glVertex2f(self.x, self.y + 65)  # Centro de la lengua
        radio = 55
        ang = pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(self.x + cos(ang_i + pi/6) * radio, (self.y + 65) + sin(ang_i + pi/6) * (radio))
        glEnd()



        glPopMatrix()