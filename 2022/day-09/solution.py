with open("day-09/input.txt") as f:
    input = [tuple(x.split()) for x in f.read().splitlines()]

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)} # replacement for big if else statement when moving the head
knots = [[0, 0] for _ in range(10)] # knots [0] == head, knots[8] == last tail
visited = [set() for _ in range(9)] # holds history for every trailing knot

def is_adjacent(h_pos, t_pos) -> bool:
    return abs(h_pos[0] - t_pos[0]) <= 1 and abs(h_pos[1] - t_pos[1]) <= 1


def move(h_pos, t_pos):
    if is_adjacent(h_pos, t_pos): return t_pos

    # move tail horizontally
    if t_pos[0] < h_pos[0]: t_pos[0] += 1 # move right
    elif t_pos[0] > h_pos[0]: t_pos[0] -= 1 # move left

    # move tail vertically
    if t_pos[1] < h_pos[1]: t_pos[1] += 1 # move up
    elif t_pos[1] > h_pos[1]: t_pos[1] -= 1 # move down
    return t_pos

for command in input:
    direction = command[0]
    steps = int(command[1])
    for i in range(abs(steps)):
        # move front knot
        knots[0][0] += directions[direction][0]
        knots[0][1] += directions[direction][1]
        
        # every next knot will be the head of the following knot, it makes the same move
        for knot in range(9):  
            leading_knot, next_knot = knots[knot], knots[knot + 1]
            next_coords = move(leading_knot, next_knot)
            visited[knot].add(tuple(next_coords))

print(len(visited[1]))
print(len(visited[8]))
