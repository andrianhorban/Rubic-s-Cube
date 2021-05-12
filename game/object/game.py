import pygame
import random

from OpenGL.GL import *
from pygame import KEYDOWN, KEYUP, K_r, K_q

from game.object.cube import Cube
from game.static.values.constants import vertices, \
    rot_piece, rot_camera, values, surfaces, colors


class game():
    def __init__(self, N, scale):
        self.N = N
        range_N = range(self.N)
        self.cubes = [Cube((x, y, z), self.N, scale)
                      for x in range_N for y in range_N for z in range_N]

    def randomize(self):
        randomlist = []
        for i in range(0, 32):
            n = random.randint(0, 9)
            randomlist.append(n)
        print(randomlist)

        for elem in randomlist:
            for key, val in values.items():
                if key == elem:
                    print("tr", key)

                    animate, action = True, rot_piece[val]
                    if animate:
                        for cube in self.cubes:
                            print(*action)
                            cube.updating(*action)

    def mainloop(self):

        corner_x, corner_y, rot_cube = 0, 0, (0, 0)
        animate, animate_corner, animate_speed = False, 0, 6
        action = (0, 0, 0)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key in rot_camera:
                        rot_cube = rot_camera[event.key]
                    if not animate and event.key in rot_piece:
                        animate, action = True, rot_piece[event.key]
                    if event.key == K_r:
                        self.randomize()
                    if event.key == K_q:
                        pygame.quit()
                        quit()

                if event.type == KEYUP:
                    if event.key in rot_camera:
                        rot_cube = (0, 0)

            corner_x += rot_cube[0]
            corner_y += rot_cube[1]

            glMatrixMode(GL_MODELVIEW)

            glLoadIdentity()

            glTranslatef(0, 0, -38)

            glRotatef(corner_y, 0, 1, 0)

            glRotatef(corner_x, 1, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            if animate:
                if animate_corner >= 90:
                    for i in self.cubes:
                        i.updating(*action)
                    animate = False
                    animate_corner = 0

            for cube in self.cubes:
                cube.draw(colors, surfaces, vertices, animate, animate_corner, *action)
            if animate:
                animate_corner = animate_corner + animate_speed

            pygame.display.flip()
            pygame.time.wait(10)
