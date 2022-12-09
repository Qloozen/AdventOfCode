ans = 0
ans2 = 0
with open("day-09/input.txt") as f:
    input = [tuple(x.split()) for x in f.read().splitlines()]
    print(input)

pos = {'h_x': 0, 'h_y': 0, 't_x': 0, 't_y': 0}
visited = set()


def is_adjacent() -> bool:
    return abs(pos['h_x'] - pos['t_x']) > 1 or abs(pos['h_y'] - pos['t_y']) > 1


def move_left(steps):
    global pos, visited
    distance = abs(pos['h_x'] - pos['t_x'])-1
    visited_coords = [visited.add((x, pos['t_y'])) for x in range(pos['t_x'], steps-1, -1)]
    visited.update(visited_coords)
    pos['t_x'] -= distance


def move_right(steps):
    global pos, visited
    pos['h_x'] += steps
    distance = abs(pos['h_x'] - pos['t_x'])-1
    visited_coords = [visited.add((x, pos['t_y'])) for x in range(pos['t_x'], distance)]
    visited.update(visited_coords)
    pos['t_x'] += distance


def move_up(steps):
    global pos, visited
    pos['h_y'] += steps
    distance = abs(pos['h_y'] - pos['t_y'])-1
    visited_coords = [visited.add((pos['t_x'], y)) for y in range(pos['t_y'], steps-1)]
    visited.update(visited_coords)
    pos['t_y'] += distance


def move_down(steps):
    global pos, visited
    pos['h_y'] -= steps
    distance = abs(pos['h_y'] - pos['t_y'])-1
    visited_coords = [visited.add((pos['t_x'], y)) for y in range(pos['t_y'], steps-1, -1)]
    visited.update(visited_coords)
    pos['t_y'] -= distance


for command in input:
    direction = input[0]
    steps = int(input[1])
    if direction == 'L':
        pos['h_x'] -= steps
        if is_adjacent():
            continue
        if pos['h_y'] == pos['t_y']:
            move_left(steps)
        else:
            if abs(pos['h_x'] - pos['h_x']) > 1)

    # elif direction == 'R':
        # if pos['h_x'] == pos['t_x']
    # elif direction == 'U':

    # elif direction == 'D':

    # print(ans)
    # print(ans2)
