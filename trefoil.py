import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def trefoil_knot(t):
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    z = -np.sin(3 * t)
    return x, y, z

def draw_knot():
    glBegin(GL_LINE_STRIP)
    for i in range(1000):
        t = 2 * np.pi * i / 1000
        x, y, z = trefoil_knot(t)
        glVertex3f(x, y, z)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            glRotatef(1, 0, 1, 0)
        if keys[K_RIGHT]:
            glRotatef(-1, 0, 1, 0)
        if keys[K_UP]:
            glRotatef(1, 1, 0, 0)
        if keys[K_DOWN]:
            glRotatef(-1, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_knot()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

