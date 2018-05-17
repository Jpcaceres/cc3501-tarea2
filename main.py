
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
    glClearColor(0.0, 0.0, 0.0, 0.0) # Color de fondo
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
    gluOrtho2D(0.0, w, 0.0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#############################################################################
# Controlador (Programa Principal)
#############################################################################

# Constantes
WINDOW_SIZE = [800, 600] # [Ancho, Alto]
FPS = 60 # Fotogramas por segundo
TITULO = "Bomberman" # Titulo del programa

# Inicialización de pantalla
initPygame(WINDOW_SIZE[0], WINDOW_SIZE[1], TITULO)
init()
reshape(WINDOW_SIZE[0], WINDOW_SIZE[1])

# Se crea el reloj del juego
clock = pygame.time.Clock()

# Se crean los modelos

# Bucle principal
while True:
    # Setea el reloj
    clock.tick(FPS)
    # Busca eventos de aplicación
    for event in pygame.event.get():
        if event.type == QUIT: # Cierra la aplicación
               exit()

    #Vuelca lo dibujado en pantalla
    pygame.display.flip()


# termina pygame (cerrar ventana)
pygame.quit()
