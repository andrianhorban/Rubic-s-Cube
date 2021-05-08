import pygame
from pygame.locals import *
from game.object.game import game
from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    pygame.init()

    flags = OPENGL | pygame.FULLSCREEN | DOUBLEBUF
    screen = pygame.display.set_mode((0, 0), flags)

    program_icon = pygame.image.load('game/static/images/program_icon.jpg')
    pygame.display.set_icon(program_icon)

    pygame.display.set_caption("Rubic's Cube")

    glEnable(GL_DEPTH_TEST)

    glClearColor(0.25, 0.65, 0.25, 1)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(40, 1.5, 0.1, 50.0)

    game_init = game(3, 1.5)

    game_init.mainloop()


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
