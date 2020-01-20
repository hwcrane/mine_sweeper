from grid import make_grid
import pygame

g = make_grid(16, 16, 40)
for line in g:
    l = ''
    for square in line:
        l = f'{l}  {square}'
    print(l)
