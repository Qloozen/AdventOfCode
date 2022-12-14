ans = 0
ans2 = 0
with open("day-14/input.txt") as f:
    '498,4 -> 498,6 -> 496,6'
    x_min = 100000 # temp workaround
    x_max = y_max = 0
    input = f.read().splitlines()
    lines = []
    for line in input: # refactor parsing
        coords = line.split(' -> ')
        to_add = []
        for coord in coords:
            x, y = list(map(int, coord.split(',')))
            if x < x_min: x_min = x
            if x > x_max: x_max = x
            if y > y_max: y_max = y
            to_add.append((y, x))
        lines.append(to_add)

part1 = True # TEMP WORKAROUND FOR NOW, SWITCH FOR PART 2

# refactor grid sizing
length = y_max + 1
side_length = length-1
left_length = abs(500 - x_min)
right_length = abs(500 - x_max)
extra_left = abs(side_length - left_length)+2 if left_length < side_length else 0
extra_right = abs(side_length - right_length)+2 if right_length < side_length else 0
subtract_x = x_min if part1 else x_min-extra_left # used to determine the actual starting index for the rocks

grid = [['.']*(x_max - x_min + 1) for i in range(y_max+1)]
grid2 = [['.']*((x_max+extra_right) - (x_min-extra_left) + 1) for i in range(y_max+3)]
for i in range(len(grid2[-1])): grid2[-1][i] = '#'

def draw_line(prev, curr, grid):
    prev_y, prev_x = prev
    curr_y, curr_x = curr
    dist_x, dist_y = abs(prev_x - curr_x), abs(prev_y - curr_y)
    if dist_x > 0:
        direction = 1 if prev_x < curr_x else -1
        for i in range(prev_x, curr_x+direction, direction):
            grid[curr_y][i - subtract_x] = '#'
    elif dist_y > 0:
        direction = 1 if prev_y < curr_y else -1
        for i in range(prev_y, curr_y+direction, direction):
            grid[i][curr_x - subtract_x] = '#'


# refactor forming rocks
for line in lines:
    prev = line[0]
    for i in range(1, len(line)):
        curr = line[i]
        draw_line(prev, curr , grid if part1 else grid2)
        prev = curr

# refactor dropping sand
def drop_sand(grid):
    is_resting = False
    x, y = 500-subtract_x, -1
    while not is_resting:
        if y+1 > len(grid)-1 or x-1 < 0 or x+1 > len(grid[0]) -1:
            return True
        # go down
        if grid[y+1][x] != '#' and grid[y+1][x] != '0':
            if y >= 0 : grid[y][x] = '.'
            grid[y+1][x] = "0"
            y += 1
            continue
        # go left down
        if  x >= 0 and grid[y+1][x-1] != '#' and grid[y+1][x-1] != '0':
            if y >= 0 : grid[y][x] = '.'
            grid[y+1][x-1] = "0"
            y += 1
            x -= 1
            continue
        #  go right down
        if x <= len(grid[0])-1 and grid[y+1][x+1] != '#' and grid[y+1][x+1] != '0':
            if y >= 0 : grid[y][x] = '.'
            grid[y+1][x+1] = "0"
            y += 1
            x += 1
            continue
        is_resting = True
    if grid[0][500-subtract_x] == "0": return True
    return False

drop_next = True
count = 0
while drop_next:
    drop_next = not drop_sand(grid if part1 else grid2)
    count += 1

print(count-1)
# print answers for both parts instead of 1

# Your puzzle answer was 817
# Your puzzle answer was 23416




