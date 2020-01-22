import random, copy


def generate_grid(w, h):
    g = []
    row = [0] * w
    for i in range(h):
        g.append(copy.deepcopy(row))

    return g


def get_square(grid, c, r):
    return grid[c][r]


def place_bomb(grid):
    c = random.randint(0, len(grid) - 1)
    r = random.randint(0, len(grid[0]) - 1)

    if get_square(grid, c, r) != '*':
        grid[c][r] = '*'
        add_numbers(grid, c, r)
    else:
        place_bomb(grid)


def add_numbers(grid, c, r):
    h = len(grid) - 1
    w = len(grid[0]) - 1
    # center left
    if r > 0 and grid[c][r - 1] != '*':
        grid[c][r - 1] += 1

    # center right
    if r < w and grid[c][r + 1] != '*':
        grid[c][r + 1] += 1

    # upper left
    if c > 0 and r > 0 and grid[c - 1][r - 1] != '*':
        grid[c - 1][r - 1] += 1

    # upper middle
    if c > 0 and grid[c - 1][r] != '*':
        grid[c - 1][r] += 1

    # upper right
    if c > 0 and r < w and grid[c - 1][r + 1] != '*':
        grid[c - 1][r + 1] += 1

    # lower left
    if c < h and r > 0 and grid[c + 1][r - 1] != '*':
        grid[c + 1][r - 1] += 1

    # lower middle
    if c < h and grid[c + 1][r] != '*':
        grid[c + 1][r] += 1

    # lower right
    if c < h and r < w and grid[c + 1][r + 1] != '*':
        grid[c + 1][r + 1] += 1


def make_grid(grid_width, grid_height, num_of_bombs):
    grid = generate_grid(grid_width, grid_height)
    for i in range(num_of_bombs):
        place_bomb(grid)
        #for line in grid:
        #    l = ''
        #    for square in line:
        #        l = f'{l}  {square}'
        #    print(l)
        #print('\n\n\n')
    return grid


def make_blank_grid(grid_width, grid_height, num_of_bombs):
    grid = generate_grid(grid_width, grid_height)
    return grid


def snake(grid, visible):
    v2 = copy.deepcopy(visible)
    for c in range(len(grid)):
        for r in range(len(grid[0])):
            if visible[c][r] and grid[c][r] == 0:
                visible = place_zeros(grid, visible, c, r)

    if visible != v2:
        snake(grid, visible)
def place_zeros(grid, v, c, r):
    h = len(grid) - 1
    w = len(grid[0]) - 1
    # center left
    if r > 0:
        v[c][r - 1] = 1

    # center right
    if r < w:
        v[c][r + 1] = 1

    # upper left
    if c > 0 and r > 0:
        v[c - 1][r - 1] = 1

    # upper middle
    if c > 0:
        v[c - 1][r] = 1

    # upper right
    if c > 0 and r < w:
        v[c - 1][r + 1] = 1

    # lower left
    if c < h and r > 0:
        v[c + 1][r - 1] = 1

    # lower middle
    if c < h:
        v[c + 1][r] = 1

    # lower right
    if c < h and r < w:
        v[c + 1][r + 1] = 1
    return v

def check_if_won(grid, flagnum, visible):
    if flagnum > 0:
        return False
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            if grid[c][r] != '*' and not visible[c][r]:
                return False
    return True
if __name__ == '__main__':
    grid_width = 16
    grid_height = 32
    num_of_bombs = 80

    grid = generate_grid(grid_width, grid_height)

    for i in range(num_of_bombs):
        place_bomb(grid)

    for line in grid:
        l = ''
        for square in line:
            l = f'{l}  {square}'
        print(l)