import re
from functools import reduce
from collections import defaultdict

# So, it has a total price of 1930.

with open("input.txt") as f:
    lines = [line for line in f.read().splitlines()]
    R = len(lines)
    C = len(lines[0])
    p1 = 0

    seen = set()
    for i in range(R):
        for j in range(C):
            if (i, j) in seen: continue
            q = [(i, j)]
            area = 0
            perimeter = 0

            while len(q) > 0:
                y, x = q.pop(0)
                c = lines[y][x]

                seen.add((y, x))
                area += 1
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny, nx = y + dy, x + dx
                    if not 0 <= ny < R:
                        perimeter += 1
                        continue
                    if not 0 <= nx < C:
                        perimeter += 1
                        continue
                    if lines[ny][nx] != c:
                        perimeter += 1
                        continue
                    if lines[ny][nx] == c and not (ny, nx) in seen and (ny, nx) not in q:
                        q.append((ny, nx))
            p1 += area * perimeter
            # print(c, area, perimeter)
    print(p1)