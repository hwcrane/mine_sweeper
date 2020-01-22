from grid import make_grid, make_blank_grid, snake, check_if_won
import pygame as pg

pg.init()
win = pg.display.set_mode((1650, 1000))

tile = pg.transform.scale(pg.image.load('./assets/tile.png'), (50, 50))
bgtile = pg.transform.scale(pg.image.load('./assets/bg_tile.png'), (50, 50))
red_tile = pg.transform.scale(pg.image.load('./assets/red_tile.png'), (50, 50))
flag = pg.transform.scale(pg.image.load('./assets/flag.png'), (50, 50))
mine = pg.transform.scale(pg.image.load('./assets/mine.png'), (50, 50))
incorrect_mine = pg.transform.scale(pg.image.load('./assets/incorrect_mine.png'), (50, 50))
background = pg.transform.scale(pg.image.load('./assets/background.png'), (1650, 1000))
sad_background = pg.transform.scale(pg.image.load('./assets/sad_background.png'), (1650, 1000))
font = pg.font.Font('freesansbold.ttf', 50)
clockfont = pg.font.Font('./assets/clock_font.ttf', 90)
fontcols = {1: (0, 0, 255), 2: (0, 128, 0), 3: (255, 0, 0), 4: (2, 13, 113), 5: (77, 0, 0), 6: (0, 139, 139),
            7: (0, 0, 0), 8: (131, 131, 131), '*': (255, 0, 0)}

g = make_grid(16, 32, 80)
g2 = make_blank_grid(16, 32, 80)
flags = make_blank_grid(16, 32, 80)
flagcount = 80
flagprifix = '0'
timer = 0
timerprifix = '00'
clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT, 1000)
play = True
start = False


def printgrid():
    win.blit(background, (0, 0))
    if flagcount // 10 == 0:
        flagprifix = '00'
    elif flagcount // 10 == 1:
        flagprifix = '0 '
    else:
        flagprifix = '0'
    win.blit(clockfont.render(f'{flagprifix}{flagcount}', True, fontcols[3]), (55, 40))

    if timer // 10 == 0:
        timerprifix = '00'
    elif timer // 10 == 1:
        timerprifix = '0 '
    elif timer // 10 < 10:
        timerprifix = '0'
    elif timer // 10 < 20:
        timerprifix = ' '
    else:
        timerprifix = ''

    win.blit(clockfont.render(f'{timerprifix}{timer}', True, fontcols[3]), (1460, 40))
    for c in range(0, len(g)):
        for r in range(0, len(g[0])):
            if flags[c][r] == 3:
                win.blit(red_tile, ((c * 50) + 25, (r * 50) + 175))
            else:
                win.blit(bgtile, ((c * 50) + 25, (r * 50) + 175))
            if (t := g[c][r]) != 0:
                if t == '*':
                    win.blit(mine, ((c * 50) + 25, (r * 50) + 175))
                else:
                    if flags[c][r] == 4:
                        win.blit(incorrect_mine, ((c * 50) + 25, (r * 50) + 175))
                    else:
                        win.blit(font.render(f'{t}', True, fontcols[t]), ((c * 50) + 35, (r * 50) + 177))
            if not g2[c][r]:
                win.blit(tile, ((c * 50) + 25, (r * 50) + 175))
            if flags[c][r] == 1:
                win.blit(flag, ((c * 50) + 25, (r * 50) + 175))

    pg.display.update()


while True:
    clock.tick(25)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.USEREVENT and timer < 999 and play and start:
            timer += 1
        if event.type == pg.MOUSEBUTTONDOWN:

            if pg.mouse.get_pressed()[0]:
                l1, l2 = pg.mouse.get_pos()

                if 175 < l1 < 875 and 39 < l2 < 139:
                    g = make_grid(16, 32, 80)
                    g2 = make_blank_grid(16, 32, 80)
                    flags = make_blank_grid(16, 32, 80)
                    flagcount = 80
                    timer = 0
                    play = True
                    start = False
                elif 25 < l1 < 1625 and 175 < l2 < 975 and play:
                    if not start:
                        start = True
                    l1 -= 25
                    l2 -= 175
                    l1, l2 = (l1 // 50, l2 // 50)

                    if not flags[l1][l2]:

                        if g[l1][l2] == '*':
                            play = False
                            for c in range(0, len(g)):
                                for r in range(0, len(g[0])):
                                    if g[c][r] == '*' and not flags[c][r]:
                                        g2[c][r] = 1

                                    if flags[c][r] and g[c][r] != '*':
                                        g2[c][r] = 1
                                        flags[c][r] = 4
                            flags[l1][l2] = 3
                        else:
                            g2[l1][l2] = 1
                            if g[l1][l2] == 0:
                                snake(g, g2)
            elif pg.mouse.get_pressed()[2]:
                l1, l2 = pg.mouse.get_pos()
                if 25 < l1 < 1625 and 175 < l2 < 975 and play and start:
                    l1 -= 25
                    l2 -= 175
                    l1, l2 = (l1 // 50, l2 // 50)
                    if not flags[l1][l2] and not g2[l1][l2] and flagcount > 0:
                        flags[l1][l2] = 1
                        flagcount -= 1
                    elif flags[l1][l2]:
                        flags[l1][l2] = 0
                        flagcount += 1
                        if check_if_won(g, flagcount, g2):
                            play = False

    printgrid()

# for line in g:
#    l = ''
#    for square in line:
#        l = f'{l}  {square}'
#    print(l)
