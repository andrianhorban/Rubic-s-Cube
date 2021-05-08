import pygame
import random

from OpenGL.GL import *
from pygame import KEYDOWN, KEYUP, K_r, K_q

from game.object.cube import Cube
from game.static.values.constants import vertices, \
    rot_slice, rot_cube, values, surfaces, colors


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

                    animate, action = True, rot_slice[val]
                    if animate:
                        for cube in self.cubes:
                            print(*action)
                            cube.update(*action)

    def mainloop(self):

        ang_x, ang_y, rot_cube = 0, 0, (0, 0)
        animate, animate_ang, animate_speed = False, 0, 6
        action = (0, 0, 0)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key in rot_cube:
                        rot_cube = rot_cube[event.key]
                    if not animate and event.key in rot_slice:
                        animate, action = True, rot_slice[event.key]
                    if event.key == K_r:
                        self.randomize()
                    if event.key == K_q:
                        pygame.quit()
                        quit()

                if event.type == KEYUP:
                    if event.key in rot_cube:
                        rot_cube = (0, 0)

            ang_x += rot_cube[0]
            ang_y += rot_cube[1]

            glMatrixMode(GL_MODELVIEW)

            glLoadIdentity()

            glTranslatef(0, 0, -38)

            glRotatef(ang_y, 0, 1, 0)

            glRotatef(ang_x, 1, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            if animate:
                if animate_ang >= 90:
                    for cube in self.cubes:
                        cube.update(*action)
                    animate, animate_ang = False, 0

            for cube in self.cubes:
                cube.draw(colors, surfaces, vertices, animate, animate_ang, *action)
            if animate:
                animate_ang += animate_speed

            pygame.display.flip()
            pygame.time.wait(10)
