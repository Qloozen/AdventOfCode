ans = 0
ans2 = 0
with open("day-09/input.txt") as f:
    input = [tuple(x.split()) for x in f.read().splitlines()]
    # print(input)

pos = {'h_x': 0, 'h_y': 0, 't_x': 0, 't_y': 0}
visited = set()
visited.add((0, 0))


def is_adjacent() -> bool:
    return abs(pos['h_x'] - pos['t_x']) <= 1 and abs(pos['h_y'] - pos['t_y']) <= 1


def move_left():
    global pos, visited
    start = pos['t_x']
    stop = pos['h_x']
    visited_coords = set()
    for x in range(start, stop, -1):
        print((x, pos['t_y']), ' ->', (pos['h_x'], pos['h_y']))
        visited_coords.add((x, pos['t_y'])) 

    visited.update(visited_coords)
    pos['t_x'] = stop+1


def move_right():
    global pos, visited
    start = pos['t_x']
    stop = pos['h_x']
    visited_coords = set()
    for x in range(start, stop):
        print((x, pos['t_y']), ' ->', (pos['h_x'], pos['h_y']))
        visited_coords.add((x, pos['t_y']))

    visited.update(visited_coords)
    pos['t_x'] = stop-1


def move_up():
    global pos, visited
    start = pos['t_y']
    stop = pos['h_y']
    visited_coords = set()
    for y in range(start, stop):
        print((pos['t_x'], y), ' ->', (pos['h_x'], pos['h_y']))
        visited_coords.add((pos['t_x'], y))

    visited.update(visited_coords)
    pos['t_y'] = stop-1


def move_down():
    global pos, visited
    start = pos['t_y']
    stop = pos['h_y']
    visited_coords = set()
    for y in range(start, stop, -1):
        print((pos['t_x'], y), ' ->', (pos['h_x'], pos['h_y']))
        visited_coords.add((pos['t_x'], y))

    visited.update(visited_coords)
    pos['t_y'] = stop+1


for command in input:
    direction = command[0]
    steps = int(command[1])
    print(command, ' begin head', (pos['h_x'], pos['h_y']))
    if direction == 'L':
        pos['h_x'] -= steps
        if is_adjacent():
            continue
        if pos['h_y'] == pos['t_y']:
            move_left()
        else:
            #  head is 1 above or 1 under
            pos['t_y'] = pos['h_y']
            pos['t_x'] -= 1
            move_left()
    if direction == 'R':
        pos['h_x'] += steps
        if is_adjacent():
            continue
        if pos['h_y'] == pos['t_y']:
            move_right()
        else:
            #  head is 1 above or 1 under
            pos['t_y'] = pos['h_y']
            pos['t_x'] += 1
            move_right() 
    if direction == 'U':
        pos['h_y'] += steps
        if is_adjacent():
            continue
        if pos['h_x'] == pos['t_x']:
            move_up()
        else:
            #  head is 1 left or 1 right
            pos['t_x'] = pos['h_x']
            pos['t_y'] += 1
            move_up()
    if direction == 'D':
        pos['h_y'] -= steps
        if is_adjacent():
            continue
        if pos['h_x'] == pos['t_x']:
            move_down()
        else:
            #  head is 1 left or 1 right
            pos['t_x'] = pos['h_x']
            pos['t_y'] -= 1
            move_down()

print(len(visited))

max_x = max(x for x, y in visited) + 1
max_y = max(y for x, y in visited)

# create a 2D grid with dots
grid = []
for y in range(max_y + 1):
    row = []
    for x in range(max_x + 1):
        if x==0 and y==0:
            row.append('s')
        elif (x, y) in visited:
            row.append("#")
        else:
            row.append(".")
    grid.append(row)

grid.reverse()
# print the grid
for row in grid:
    print(" ".join(row))
