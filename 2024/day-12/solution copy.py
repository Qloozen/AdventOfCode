import re
from functools import reduce
from collections import defaultdict, Counter

# So, it has a total price of 1930.
# Adding these together produces its new total price of 1206.

with open("input.txt") as f:
    lines = [line for line in f.read().splitlines()]
    R = len(lines)
    C = len(lines[0])
    p1 = 0
    p2 = 0
    tb = {(-1, 0), (1, 0)}
    lr = {(0, -1), (0, 1)} 


    seen = set()
    for i in range(R):
        for j in range(C):
            if (i, j) in seen: continue
            q = [(i, j)]
            area = 0
            total_perimeter = 0
            sides = 0
            outer_blocks = defaultdict(list)
            outer_parallel = False

            while len(q) > 0:
                y, x = q.pop(0)
                c = lines[y][x]

                seen.add((y, x))
                area += 1
                edges_d = []

                if (y, x) in [(7, 0)]:
                    t = 0
                has_parallel = False
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny, nx = y + dy, x + dx
                    if not 0 <= ny < R:
                        edges_d.append((dy, dx))
                        continue
                    if not 0 <= nx < C:
                        edges_d.append((dy, dx))
                        continue
                    if lines[ny][nx] != c:
                        outer_blocks[(ny, nx)].append((dy, dx))
                        edges_d.append((dy, dx))
                        continue
                    if lines[ny][nx] == c and not (ny, nx) in seen and (ny, nx) not in q:
                        q.append((ny, nx))


                if tb.issubset(edges_d) or lr.issubset(edges_d):
                    has_parallel = True

            

                edges = len(edges_d)
                total_perimeter += edges
                if edges == 2 and not has_parallel: 
                    sides += 1
                elif edges == 3:
                    sides += 2
                elif edges == 4:
                    sides += 4

            for k, v in outer_blocks.items():
                edges_out = len(v)
                has_parallel_out = tb.issubset(v) or lr.issubset(v)
                if edges_out == 2 and not has_parallel_out:    
                    sides += 1
                elif edges_out == 3:
                    sides += 2
                elif edges_out == 4:
                    sides += 4

            print(c, area, sides)
            p1 += area * total_perimeter
            p2 += area * sides
    print(p1) 
    print(p2)

    # Your puzzle answer was 1381056.
    
    #not 850404
    #not 841626 (to high)

