with open("input.txt") as f:
    DIR = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    
    input = f.read().split("\n\n")
    instructions = ''.join([line.strip() for line in input[1]])
    pos = (0, 0)
    grid = []
    for i, line in enumerate(input[0].splitlines()):
        if '@' in line:
            pos = (i, line.index("@"))
        grid.append(list(line))

    R = len(grid)
    C = len(grid[0])
    
    for d in instructions:
        y, x = pos
        dy, dx = DIR[d]
        ny, nx = dy + y, dx + x

        if grid[ny][nx] == '#': continue
        if grid[ny][nx] == 'O':
            space_y, space_x = dy + ny, dx + nx
            while True:
                if grid[space_y][space_x] == '#': break
                if grid[space_y][space_x] == '.':
                    grid[space_y][space_x] = 'O'

                    pos = (ny, nx)
                    grid[ny][nx] = '@'
                    grid[y][x] = '.'
                    break   
                else:
                    space_y, space_x = dy + space_y, dx + space_x
        else:
            pos = (ny, nx)
            grid[ny][nx] = '@'
            grid[y][x] = '.'
    
    p1 = 0

    for i in range(1, R-1):
        for j in range(1, C-1):
            if grid[i][j] == "O":
                p1 += 100 * i + j
    print(p1)
                  
# Your puzzle answer was 1485257.