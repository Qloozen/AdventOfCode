import re
from collections import defaultdict
from PIL import Image


with open("input.txt") as f:
    R = 103
    C = 101

    positions = defaultdict(list)

    for line in f.read().splitlines():
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        positions[(px, py)].append((vx, vy))

for i in range(10000): 
    image = Image.new("RGB", (C, R), (15, 15, 35))
    pixels = image.load()
    new_positions = defaultdict(list)
    for pos, robots in positions.items():
        while len(robots) > 0:
            robot = robots.pop()
            vx, vy = robot
            px, py = (pos[0] + vx) % C, (pos[1] + vy) % R
            new_positions[(px, py)].append(robot)
    positions = new_positions
    for k, v in positions.items():
        pixels[k[0], k[1]] = (153, 255, 153)

    image.save(f'./renders/{i+1}.png')



    


