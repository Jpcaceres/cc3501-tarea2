
# coding=utf-8
"""
Bomberman
@Autor Juan Cáceres
"""
#############################################################################
# Importación de librerías
#############################################################################

import pygame
from pygame.locals import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *

from Vista import *
from Pug import *
from Muros1 import *
from Muros2 import *
from Bombas import *

#############################################################################
# Funciones Gráficas
#############################################################################

def initPygame(w, h, title):
    """
    Inicia Pygame
    :param w: Ancho de la ventana (px)
    :param h: Alto de la ventana (px)
    :param title: Título de la ventana
    :return: None
    """
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centra la ventana
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)  # Crea la ventana
    pygame.display.set_caption(title)  # Título de la ventana

def init():
    """
    Inicia openGL
    :return: None
    """
    glClearColor(1.0, 1.0, 1.0, 0.0) # Color de fondo
    glClearDepth(1.0) # Profundidad de dibujo
    glDisable(GL_DEPTH_TEST) # Se inabilita depth test
    glShadeModel(GL_SMOOTH) # Activa el dibujo suave
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Corrección de la matriz de perspectiva
    glEnable(GL_BLEND) # Transparencia
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST) # Antialiasing

def reshape(w, h):
    """
    Maneja la pantalla openGL
    :param w: Ancho de la ventana (px)
    :param h: Alto de la ventana (px)
    :return: None
    """
    h = max(h, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, w, 0.0, h) #define la matriz de proyeccion ortogonal 2D
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#############################################################################
# Controlador (Programa Principal)
#############################################################################

# Constantes
WINDOW_SIZE = [800, 600] # [Ancho, Alto]
FPS = 90 # Fotogramas por segundo
TITULO = "Bomberman" # Titulo del programa

# Inicialización de pantalla
initPygame(WINDOW_SIZE[0], WINDOW_SIZE[1], TITULO)
init()
reshape(WINDOW_SIZE[0], WINDOW_SIZE[1])
clock = pygame.time.Clock() # Se crea el reloj del juego
run = True # condicion booleana True para iterar

# Se crean los modelos
pug = Pug(300, 300, 10, 10)
vista = Vista()

# infinitamente hasta quebrar el ciclo con otra condicion
while run:
    vista.dibujar(pug)

    for event in pygame.event.get():
        # para dada evento almacenado en "obtener eventos"
        if event.type == QUIT: # cick sobre cerrar para salir
               run = False
        if event.type == KEYDOWN: # al presionar una tecla
            if event.key == K_ESCAPE: # si se presiona ESC
                run = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        pug.moverIzquierda()
    elif keys[K_RIGHT]:
        pug.moverDerecha()
    elif keys[K_DOWN]:
        pug.moverAbajo()
    elif keys[K_UP]:
        pug.moverArriba()

    pygame.display.flip() # redibuja la ventana con el buffer almacenado
    clock.tick(FPS)  # Setea el reloj del juego para ajustar a la cantidad de FPS dados


