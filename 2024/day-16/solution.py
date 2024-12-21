
import heapq
from collections import namedtuple
with open("input.txt") as f:
    Step = namedtuple("Step", "cost y x dir")


    start = (0, 0)
    grid = []
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
        grid.append(list(line))
    R = len(grid)
    C = len(grid[0])
    
    
    def bfs(start):
        seen = set()
        q = [Step(cost=0, y=start[0], x=start[1], dir=1)]
        scores = []

        while len(q) > 0:
            pos = heapq.heappop(q)
            cost, y, x, prev_d = pos

            if grid[y][x] == "E":
                print(pos)
                scores.append(cost)
                continue
            
            if (y, x, prev_d) in seen: continue
            
            seen.add((y, x, prev_d))

            for d_i, (dy, dx) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]): 
                ny, nx = y + dy, x + dx
                if not(0 <= ny < R and 0 <= nx < C): continue
                if grid[ny][nx] == "#": continue

                new_cost = cost + (1000 if d_i != prev_d else 0)
                new_cost += 1
                next_pos = Step(cost=new_cost, y=ny, x=nx, dir=d_i)
                if next_pos in q: continue
                heapq.heappush(q, next_pos)
        return sorted(scores)
    
    sorted_scores = bfs(start)
    # print(sorted_scores)
    print(sorted_scores[0])

# Your puzzle answer was 89460.
        

