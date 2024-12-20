with open("input.txt") as f:

    start = (0, 0)
    grid = []
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
        grid.append(list(line))
    R = len(grid)
    C = len(grid[0])

    print(grid[start[0]][start[1]])
    print(start)
    
    
    def bfs(start):
        seen = set()
        q = [(start[0], start[1], 0, 1, 0)] # y, x, dist,  prev_d,  turns
        scores = []

        while len(q) > 0:
            # print(len(q))
            pos = q.pop(0)
            y, x, dist, prev_d, turns = pos

            if grid[y][x] == "E":
                print(pos)
                scores.append(1000*turns+dist)
                continue

            
            seen.add((y, x, prev_d))

            for d_i, (dy, dx) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]): # 0: north, 1: east, 2: south, 3: west
                ny, nx = y + dy, x + dx
                if not(0 <= ny < R and 0 <= nx < C): continue
                if grid[ny][nx] == "#": continue

                next_turns = turns + (1 if d_i != prev_d else 0)
                next_pos = (ny, nx, dist + 1, d_i, next_turns)
                if (ny, nx, d_i) in seen and grid[ny][nx] != "E": continue
                if next_pos in q: continue
                q.append(next_pos)
        return sorted(scores)


    sorted_scores = bfs(start)
    print(sorted_scores)
    print(sorted_scores[0])

    # too high 99432
    # not 97432 too high
        

