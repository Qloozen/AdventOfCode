
import heapq
from collections import namedtuple
with open("ex2.txt") as f:
    Step = namedtuple("Step", "cost y x dir path")
    #SOLUTION TOO SLOW FOR INPUT

    start = (0, 0)
    grid = []
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
        grid.append(list(line))
    R = len(grid)
    C = len(grid[0])
    print(f'R: {R}, C: {C}')
    
    
    def bfs(start):
        q = [Step(cost=0, y=start[0], x=start[1], dir=1, path = set())]
        scores = []

        while len(q) > 0:
            pos = heapq.heappop(q)
            cost, y, x, prev_d, path = pos
            if (cost % 10 == 0):
                print(cost)
                

            if grid[y][x] == "E":
                print(cost)
                if len(scores) > 0 and scores[-1][0] != cost:
                    break
                path.add((y, x))
                scores.append(pos)
                continue
            
            if (y, x) in path: continue
            # if (y, x, prev_d) in seen: continue
            
            path.add((y, x))
            # seen.add((y, x, prev_d))

            for d_i, (dy, dx) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]): 
                ny, nx = y + dy, x + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                # print(ny, nx)
                if grid[ny][nx] == "#": continue

                new_cost = cost + (1000 if d_i != prev_d else 0)
                new_cost += 1
                next_pos = Step(cost=new_cost, y=ny, x=nx, dir=d_i, path=path.copy())
                t = list(map(lambda x: (x[0], x[1], x[2]), q))
                if (cost, ny, nx) in t: 
                    continue
                heapq.heappush(q, next_pos)
        return sorted(scores, key= lambda s: s[0])
    
    sorted_scores = bfs(start)
    # print(sorted_scores)
    print(sorted_scores[0][0])

# Your puzzle answer was 89460.

    all_steps = set()

    for step in sorted_scores:
        cost, y, x, prev_d, path = step
        all_steps |= path

    print(len(all_steps))
        
        # print(f'\n---best path version---')
        # for i in range(R):
        #     line = ''
        #     for j in range(C):
        #         c = grid[i][j]
        #         if c != '#': 
        #             if (i, j) in path:
        #                 line += 'O'
        #             else: line+= '.'
        #         else:
        #             line += '#'
        #     print(line)
        

