with open("input.txt") as f:
    DIR = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    input = f.read().split("\n\n")
    instructions = ''.join([line.strip() for line in input[1]])
    pos = (0, 0)
    grid = []
    for i, line in enumerate(input[0].splitlines()):
        row = []
        for c in line:
            if c == '#': row += ['#', '#']
            elif c == 'O': row += ['[', ']'] 
            elif c == '.': row += ['.', '.'] 
            elif c == '@':
                pos = (i, len(row))
                row += ['@', '.'] 

        grid.append(row)

    R = len(grid)
    C = len(grid[0])

    for d in instructions:
        y, x = pos
        dy, dx = DIR[d]
        ny, nx = dy + y, dx + x
        
        if grid[ny][nx] == '#': continue
        if grid[ny][nx] in ['[', ']']:
            if grid[ny][nx] == '[': first_block = ((ny, nx), (ny, nx + 1))
            elif grid[ny][nx] == ']': first_block = ((ny, nx - 1), (ny, nx))
            
            seen = []
            q = [(first_block)]
            can_move = True
            while len(q) > 0: 
                block = q.pop(0) 
                seen.append(block)
                (ly, lx), (ry, rx) = block 

                if d == '>':
                    np = (ry + dy, rx + dx)
                    c = grid[np[0]][np[1]]
                    if c == '#': 
                        can_move = False
                        break
                    if c == '[': q.append(((np), (np[0] + dy, np[1] + dx)))
                elif d == '<':
                    np = (ly + dy, lx + dx)
                    c = grid[np[0]][np[1]]
                    if c == '#': 
                        can_move = False
                        break
                    if c == ']': q.append(((np[0] + dy, np[1] + dx), (np)))
                elif d == '^' or d == "v":
                    l_np = (ly + dy, lx)
                    r_np = (ry + dy, rx)
                    cl = grid[l_np[0]][l_np[1]]
                    cr = grid[r_np[0]][r_np[1]]

                    if cl == "#" or cr == '#':
                        can_move = False
                        break
                    if cl == '[' and cr == ']':
                        q.append((l_np, r_np))
                        continue
                    if cl == ']':
                        q.append(((l_np[0], l_np[1] - 1), l_np))
                    if cr == '[':
                        q.append((r_np, (r_np[0], r_np[1] + 1)))
            
            if can_move:
                moved = set()
                for l, r in reversed(seen):
                    if (l, r) in moved: continue
                    nl_pos = (l[0] + dy, l[1] + dx)
                    nr_pos = (r[0] + dy, r[1] + dx)
                    cl = grid[l[0]][l[1]]
                    cr = grid[r[0]][r[1]]
                    grid[l[0]][l[1]] = '.'
                    grid[r[0]][r[1]] = '.'
                    grid[nl_pos[0]][nl_pos[1]] = cl
                    grid[nr_pos[0]][nr_pos[1]] = cr
                    
                    moved.add((l, r))

                pos = (ny, nx)
                grid[ny][nx] = '@'
                grid[y][x] = '.'
        else:
            pos = (ny, nx)
            grid[ny][nx] = '@'
            grid[y][x] = '.'
    p2 = 0
    for i in range(1, R-1):
        for j in range(1, C-1):
            if grid[i][j] == "[":
                p2 += 100 * i + j
    print(p2)
                  
    
# Your puzzle answer was 1475512.