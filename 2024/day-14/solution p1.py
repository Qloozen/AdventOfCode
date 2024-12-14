import re
from collections import Counter

with open("input.txt") as f:
    R = 103
    C = 101

    positions = []
    for line in f.read().splitlines():
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        px, py = (px + vx * 100) % C, (py + vy * 100) % R
            
        positions.append((px, py))

    counts = Counter(positions)
    q1, q2, q3, q4 = 0, 0, 0, 0

    for (x, y), v in counts.items():
        if y < R // 2 and x < C // 2: q1 += v
        if y < R // 2 and x > C // 2: q2 += v
        if y > R // 2 and x < C // 2: q3 += v
        if y > R // 2 and x > C // 2: q4 += v



    print(q1 * q2 * q3 * q4)

# Your puzzle answer was 224969976.
    