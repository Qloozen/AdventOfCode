ans = 0
ans2 = 0
with open("day-10/input.txt") as f:
    input = [line.split() for line in f.read().splitlines()]

x = 1
cycle_count = 0
strength_list = []
for command in input:
    type = command[0]
    value = int(command[1]) if len(command) > 1 else 0
    if type == 'noop':
        if (cycle_count + 1) % 40 == 20:
            t = x * (cycle_count + 1)
            strength_list.append(t)
        cycle_count += 1
    elif type == 'addx':
        if (cycle_count + 1) % 40 == 20:
            t = x * (cycle_count + 1)
            strength_list.append(t)

        cycle_count += 2

        if cycle_count % 40 == 20:
            t = x * cycle_count
            strength_list.append(t)

        x += value

print(sum(strength_list[:6]))

x = 1
cycle_count = 0
grid = []
base_line = ['.' for _ in range(40)]
line = base_line.copy()
for command in input:
    type = command[0]
    value = int(command[1]) if len(command) > 1 else 0
    sprite = (x-1, x, x+1)
    if type == 'noop':
        if cycle_count in sprite:
            line[cycle_count] = '#'
        cycle_count += 1
        if cycle_count == 40:
            grid.append(''.join(line))
            line = base_line.copy()
            cycle_count = 0
    elif type == 'addx':
        if cycle_count in sprite:
            line[cycle_count] = '#'
        cycle_count += 1
        if cycle_count == 40:
            grid.append(''.join(line))
            line = base_line.copy()
            cycle_count = 0

        if cycle_count in sprite:
            line[cycle_count] = '#'
        cycle_count += 1
        if cycle_count == 40:
            grid.append(''.join(line))
            line = base_line.copy()
            cycle_count = 0
        x += value

for line in grid:
    print(line)
