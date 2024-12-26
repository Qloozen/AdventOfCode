
import heapq
from collections import namedtuple

with open("input.txt") as f:
    Step = namedtuple("Step", "cost pos dir path")

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
        q = [Step(cost=0, pos=start, dir=1, path=set())]
        best_path = None
        visited = set()

        while len(q) > 0:
            pos = heapq.heappop(q)
            cost, (y, x), prev_d, path = pos

            collides = [item for item in q if item[:-1] == pos[:-1]] 
            if len(collides) > 0:
                index = q.index(collides[0])
                visited_current = {(item[0], item[1]) for item in path}
                visited_other = {(item[0], item[1]) for item in collides[0][3]}
                q[index] = (*collides[0][:-1], visited_current | visited_other)
                continue

            if (y, x, prev_d) in visited:
                continue

            visited.add((y, x, prev_d))
            path = path.copy()
            path.add((y, x, prev_d))

            if grid[y][x] == "E":
                if best_path is not None and best_path[0] != cost: break
                best_path = Step(*pos[:-1], path)
                break

            for d_i, (dy, dx) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]): 
                ny, nx = y + dy, x + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                if grid[ny][nx] == "#": continue

                
                new_cost = cost + (1000 if d_i != prev_d else 0)
                new_cost += 1
                next_pos = Step(cost=new_cost, pos=(ny, nx), dir=d_i, path=path)
                heapq.heappush(q, next_pos)
        return best_path
    
    best_path = bfs(start)
    print(best_path[0])
    print(len(best_path[3]))


# Your puzzle answer was 89460.
# Your puzzle answer was 504.


