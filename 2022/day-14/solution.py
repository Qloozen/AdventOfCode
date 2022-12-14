ans = 0
ans2 = 0
with open("day-14/input.txt") as f:
    '498,4 -> 498,6 -> 496,6'
    x_min = 100000
    x_max = y_max = 0
    input = f.read().splitlines()
    lines = []
    for line in input:
        coords = line.split(' -> ')
        to_add = []
        for coord in coords:
            x, y = list(map(int, coord.split(',')))
            if x < x_min: x_min = x
            if x > x_max: x_max = x
            if y > y_max: y_max = y
            to_add.append((x, y))
        lines.append(to_add)

t = x_max - x_min + 1
grid = [['.']*(x_max - x_min + 1)]*y_max

def draw_horizontal(y, prev, curr, grid):
    for i in range(prev, curr + 1, 1):
        grid[y][i] = '#'

def draw_vertical(x, prev, curr, grid):
    for i in range(prev, curr + 1, 1):
        grid[i][x] = '#'

for line in lines:
    prev_y, prev_x = line[0]
    for i in range(1, len(line)+1, 1):
        y, x = line[i]
        if abs(prev_y - y) > 0:
            draw_vertical(x, prev_y, y, grid)
        elif abs(prev_x - x) > 0:
            draw_horizontal(y, prev_x, x, grid)





