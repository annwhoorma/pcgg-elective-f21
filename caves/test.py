from math import pi
import matplotlib.pyplot as plt
from random import randint
from mpl_toolkits import mplot3d
import numpy as np

class Point:
    def __init__(self, x, y):
        self.coords = [x, y]
    
    def add(self, x, y):
        self.coords[0] += x
        self.coords[1] += y


class LSystem:
    def __init__(self):
        self.direction = [1, 1]
        self.angle = pi / 4

        self.alphabet = {
            'F': [1, 1],
            'B': [-1, -1],
            'K': [-1, 1],
            'P': [1, -1],
            'R': [1, 0],
            'L': [-1, 0],
            'U': [0, 1],
            'D': [0, -1]
        }

        self.macros = {
            # ('X') - repeat X 0 or more times
            # ['X'] - repeat X 1 or more times
            # X = repeat once (doesnt exist yet)
            'scale': '(U)[F](R)[P](D)'
        }

    def draw_cave(self, path, start=[0, 0], rand_seed=3):
        cave_parts = self.find_all_subpaths_between(path, '[', ']')
        coords_x = [start[0]]
        coords_y = [start[1]]
        for part in cave_parts:
            for _ in range(randint(0, rand_seed)):
                next_point = self.alphabet[part]
                coords_x.append(coords_x[-1] + next_point[0])
                coords_y.append(coords_y[-1] + next_point[1])
        return coords_x, coords_y

    def parse_as_tree(self, path):
        pass

    # generalize: to take [['[', ']', 1], ['(', ')', 0]]
    def find_all_subpaths_between(self, path: str, char1: str, char2: str, inclusive=False):
        children = []
        in_substring = False
        # also if number of occurences is different
        if char1 not in path or char2 not in path:
            return

        for char in path:
            if char == char1 and not in_substring:
                children.append(char1 if inclusive else '')
                in_substring = True

            elif char == char2 and in_substring:
                children[-1] += char2 if inclusive and children else ''
                in_substring = False

            elif in_substring:
                children[-1] += char
        return children


class Cave:
    def __init__(self, children=[], repeat_at_least=0):
        pass



lsys = LSystem()
x, y = [], []
start = [0, 0]
parabola = lambda x: x**2

for i in range(-100, 100):
    if x and y:
        start = [x[-1], y[-1]]
    newx, newy = lsys.draw_cave('[U][F][R][P][D]', start, randint(0, parabola(i)))
    x += newx
    y += newy

plt.plot(x, y)
plt.show()

