from collections import deque

with open("input.txt") as f:
    grid = [line for line in f.read().splitlines()]
    R = len(grid)
    C = len(grid[0])
    p1 = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(pos, grid):
        # part 1
        q = deque([pos])
        area = 0
        perimeter = 0
        region = set()

        while len(q) > 0:
            y, x = q.popleft()
            c = grid[y][x]

            if (y, x) in region: continue
            region.add((y, x))
            area += 1
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < R and 0 <= nx < C): 
                    perimeter += 1
                    continue
                if grid[ny][nx] != c:
                    perimeter += 1
                    continue
                if grid[ny][nx] == c and not (ny, nx) in region: 
                    q.append((ny, nx))
        return (area, perimeter, region)
    
    def get_inward_fences(pos, region):
        # part 2
        y, x = pos
        inward_fences = [] 

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if (ny, nx) in region: 
                inward_fences.append((ny, nx))
        return inward_fences if len(inward_fences) > 1 else []
    
    def parallel_pos(fences):
        # part 2
        if len(fences) != 2 : return False
        a, b, = fences

        return abs(a[0] - b[0]) == 2 or abs(a[1] - b[1]) == 2

    def get_corners(fences):
        # part 2
        connected_fences = len(fences)
        if connected_fences < 2: return 0
        if connected_fences == 2: return 0 if parallel_pos(fences) else 1
        if connected_fences == 3: return 2
        if connected_fences == 4: return 4

    def check_diagonal(pos, grid, outward_fences): 
        # part 2
        y, x = pos
        c = grid[y][x]
        diagonals = []
        for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < R and 0 <= nx < C) or grid[ny][nx] != c: continue
            other_fences = []

            for ddy, ddx in dirs:
                nny, nnx = ny + ddy, nx + ddx
                if not (0 <= nny < R and 0 <= nnx < C): continue
                if grid[nny][nnx] != c:
                    other_fences.append((nny, nnx))
            if len(set(outward_fences) & set(other_fences)) == 2: 
                diagonals.append((ny, nx))
        
        return (False, None) if len(diagonals) == 0 else (True, diagonals)
    
    def calculate_sides(region, grid):
        # part 2
        visited_outside = set()
        total_corners = 0
        diagonals = []

        for plant in region:
            y, x = plant
            c = grid[y][x]

            outward_fences = []
            corners = 0
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < R and 0 <= nx < C): 
                    outward_fences.append((ny, nx))
                    continue
                if grid[ny][nx] != c:
                    outward_fences.append((ny, nx))
                    
                    if (ny, nx) not in visited_outside:
                        inward_fences = get_inward_fences((ny, nx), region)
                        corners += get_corners(inward_fences)
                        visited_outside.add((ny, nx))
                    continue
            
            is_diagonal, diagonal_with = check_diagonal((y, x), grid, outward_fences)
            if is_diagonal:
                diagonals.append((y, x)) 
                for diagonal in diagonal_with:
                    if diagonal in diagonals:
                        total_corners -= 2

            outer_corners = get_corners(outward_fences)  
            corners += outer_corners
            total_corners += corners

        return total_corners

    seen = set()
    p2 = 0
    for i in range(R):
        for j in range(C):
            if (i, j) in seen: continue
            area, perimeter, region = bfs((i, j), grid)
            p1 += area * perimeter
            seen |= region

            # Part 2
            sides = calculate_sides(region, grid)
            p2 += area * sides
    print(p1)
    print(p2)

    # Your puzzle answer was 1381056.
    # Your puzzle answer was 834828.

