from grid import make_grid, make_blank_grid, snake
import pygame as pg


pg.init()
win = pg.display.set_mode((800, 800))

tile = pg.transform.scale(pg.image.load('./assets/tile.png'), (50, 50))
bgtile = pg.transform.scale(pg.image.load('./assets/bg_tile.png'), (50, 50))
flag = pg.transform.scale(pg.image.load('./assets/flag.png'), (50, 50))

font = pg.font.Font('freesansbold.ttf', 50)
fontcols = {1: (0, 0, 255), 2: (0, 128, 0), 3: (255, 0, 0), 4: (2, 13, 113), 5: (77, 0, 0), 6: (0, 139, 139),
            7: (0, 0, 0), 8: (131, 131, 131), '*': (255, 0, 0)}

g = make_grid(16, 16, 40)
g2 = make_blank_grid(16, 16, 40)
flags = make_blank_grid(16, 16, 40)

def printgrid():
    for c in range(0, 16):
        for r in range(0, 16):

            win.blit(bgtile, (c * 50, r * 50))
            if (t := g[c][r]) != 0:
                win.blit(font.render(f'{t}', True, fontcols[t]), ((c * 50) + 10, (r * 50) + 2))
            if not g2[c][r]:
                win.blit(tile, (c * 50, r * 50))
            if flags[c][r]:
                win.blit(flag, (c * 50, r * 50))
    pg.display.update()


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:

            if pg.mouse.get_pressed()[0]:
                l1, l2 = pg.mouse.get_pos()
                l1, l2 = (l1//50, l2//50)
                if not flags[l1][l2]:
                    g2[l1][l2] = 1
                    if g[l1][l2] == 0:
                        snake(g, g2)
            elif pg.mouse.get_pressed()[2]:
                l1, l2 = pg.mouse.get_pos()
                l1, l2 = (l1 // 50, l2 // 50)
                if not flags[l1][l2] and not g2[l1][l2]:
                    flags[l1][l2] = 1
                else:
                    flags[l1][l2] = 0

    printgrid()

# for line in g:
#    l = ''
#    for square in line:
#        l = f'{l}  {square}'
#    print(l)
