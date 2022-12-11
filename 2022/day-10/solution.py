ans = 0
with open("day-10/input.txt") as f:
    input = [line.split() for line in f.read().splitlines()]

x = 1
cycle_count = 0
strength_list = []
CTR_display = ''
current_line = ''

def process_cycle(strength_list):
    global cycle_count, CTR_display
    print_pixel() # part 2
    cycle_count += 1
    strength_list.append(x * cycle_count)

def print_pixel(): # part 2
    global CTR_display, current_line
    sprite = (x-1, x, x+1)
    cycle_index = cycle_count % 40
    pixel = '#' if cycle_index in sprite else '.'
    current_line = ''.join([current_line, pixel])
    if cycle_index == 39:
        CTR_display = '\n'.join([CTR_display, current_line])
        current_line = ''

for command in input:
    type, value = command[0], int(command[1]) if len(command) > 1 else 0
    process_cycle(strength_list)
    if type == 'addx':
        process_cycle(strength_list)
        x += value

ans = sum([strength_list[i] for i in range (19, 220, 40)])
print(ans)
print(CTR_display)

# Your puzzle answer was 15220
# Your puzzle answer was RFZEKBFA
