from pygame.locals import *


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (1, 0.5, 0),
    (1, 1, 0),
    (1, 1, 1),
    (0, 0, 1)
)

rot_cube = {
    K_UP: (-1, 0),
    K_DOWN: (1, 0),
    K_LEFT: (0, -1),
    K_RIGHT: (0, 1)
}

rot_slice = {
    K_1: (0, 0, 1),
    K_2: (0, 1, 1),
    K_3: (0, 2, 1),
    K_4: (1, 0, 1),
    K_5: (1, 1, 1),
    K_6: (1, 2, 1),
    K_7: (2, 0, 1),
    K_8: (2, 1, 1),
    K_9: (2, 2, 1),
    K_F1: (0, 0, -1),
    K_F2: (0, 1, -1),
    K_F3: (0, 2, -1),
    K_F4: (1, 0, -1),
    K_F5: (1, 1, -1),
    K_F6: (1, 2, -1),
    K_F7: (2, 0, -1),
    K_F8: (2, 1, -1),
    K_F9: (2, 2, -1),
}

values = {
    -9: K_F9,
    -8: K_F8,
    -7: K_F7,
    -6: K_F6,
    -5: K_F5,
    -4: K_F4,
    -3: K_F3,
    -2: K_F2,
    -1: K_F1,
    0: K_1,
    9: K_9,
    8: K_8,
    7: K_7,
    6: K_6,
    5: K_5,
    4: K_4,
    3: K_3,
    2: K_2,
    1: K_1
}