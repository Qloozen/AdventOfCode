from collections import deque, defaultdict


with open("input.txt") as f:
    
    start = (0, 0)
    G = []
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line): 
            if c == "S":
                start = (i, j)
        G.append(list(line))
    R = len(G)
    C = len(G[0])

    def bfs(grid):
        Q = deque()
        Q.append((*start, 0))

        seen = set()
        while Q:
            y, x, dist = Q.popleft()

            if grid[y][x] == 'E':
                return dist


            if (y, x) in seen: continue
            seen.add((y, x))

            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx  = y + dy, x + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                if grid[ny][nx] == '#': continue
                Q.append((ny, nx, dist + 1))
        

    def printgrid(G):
        print('\n----Grid----')
        for i in range(R):
            line = ''
            for j in range(C):
                line += G[i][j]
            print(line)

    no_cheats = bfs(G)

    done = set()
    counter = defaultdict(int)
    for i in range(1, R-1):
        # print(f'{i} of {R-1}')
        for j in range(1, C-1):
            if G[i][j] == '#':
                G[i][j] = '*'
                cheat = bfs(G)
                counter[no_cheats - cheat] += 1
                G[i][j] = '#'
    
    p1 = 0
    for k, v in counter.items():
        if k >= 100: p1 += v
    print(p1)



    
            
                
