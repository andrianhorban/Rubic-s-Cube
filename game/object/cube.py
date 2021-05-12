from OpenGL.GL import *

from game.static.values.constants import vertices, colors


class Cube():

    def __init__(self, id, size, scale):
        self.size = size
        self.scale = scale
        self.start_pos = [*id]
        self.pos = [*id]
        self.rotating = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def is_affected(self, axle, piece):
        b_check = self.pos[axle] == piece
        return b_check

    def updating(self, axle, piece, direction):

        if not self.is_affected(axle, piece):
            return None

        i_temp = axle + 1
        j_temp = axle + 2
        i, j = i_temp % 3, j_temp % 3
        print(i, j)
        for k in range(3):
            self.rotating[k][j], self.rotating[k][i] = self.rotating[k][i] * direction, -self.rotating[k][j] * direction

        self.pos[i], self.pos[j] = (
            self.pos[j] if direction < 0 else self.size - 1 - self.pos[j],
            self.pos[i] if direction > 0 else self.size - 1 - self.pos[i])

        print(self.rotating)

    def transform_matrix(self):
        T = [(l - (self.size - 1) / 2) * 2.08 * self.scale for l in self.pos]
        A = [[k * self.scale for k in l] for l in self.rotating]
        return [*A[0],
                0,
                *A[1],
                0,
                *A[2],
                0,
                *T,
                1]

    def draw(self, colors, surface, vertices, animate, corner, axle, piece, direction):

        glPushMatrix()
        if animate and self.is_affected(axle, piece):
            glRotatef(corner * direction, *[1 if i == axle else 0 for i in range(3)])
        glMultMatrixf(self.transform_matrix())

        glBegin(GL_QUADS)
        for i in range(len(surface)):
            glColor3fv(colors[i])
            for j in surface[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()
