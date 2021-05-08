from OpenGL.GL import *

from game.static.values.constants import vertices, colors


class Cube():

    def __init__(self, id, N, scale):
        self.N = N
        self.scale = scale
        self.init_i = [*id]
        self.current_i = [*id]
        self.rot = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def is_affected(self, axis, slice):
        return self.current_i[axis] == slice

    def update(self, axis, slice, direction):

        if not self.is_affected(axis, slice):
            return

        i, j = (axis + 1) % 3, (axis + 2) % 3
        print(i, j)
        for k in range(3):
            print(self.rot)
            self.rot[k][i], self.rot[k][j] = -self.rot[k][j] * direction, self.rot[k][i] * direction

        self.current_i[i], self.current_i[j] = (
            self.current_i[j] if direction < 0 else self.N - 1 - self.current_i[j],
            self.current_i[i] if direction > 0 else self.N - 1 - self.current_i[i])

    def transform_matrix(self):

        scaleA = [[s * self.scale for s in a] for a in self.rot]
        scaleT = [(p - (self.N - 1) / 2) * 2.1 * self.scale for p in self.current_i]
        return [*scaleA[0], 0, *scaleA[1], 0, *scaleA[2], 0, *scaleT, 1]

    def draw(self, colors, surface, vertices, animate, angle, axis, slice, direction):

        glPushMatrix()
        if animate and self.is_affected(axis, slice):
            glRotatef(angle * direction, *[1 if i == axis else 0 for i in range(3)])
        glMultMatrixf(self.transform_matrix())

        glBegin(GL_QUADS)
        for i in range(len(surface)):
            glColor3fv(colors[i])
            for j in surface[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()

