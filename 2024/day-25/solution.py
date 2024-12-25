with open("input.txt") as f:
    grids = f.read().split('\n\n')
    grids = [grid.splitlines() for grid in grids]

    locks = []
    keys = []

    R = len(grids[0])
    C = len(grids[0][0])

    for grid in grids:
        assert(len(grid) == R)
        assert(len(grid[0]) == C)
        
        is_lock = all(c == '#'for c in grid[0])

        nums = []
        for c in range(C):
            length = sum([1 for r in range(R) if grid[r][c] == '#'])
            nums.append(length-1)

        if is_lock: locks.append(tuple(nums))
        else : keys.append(tuple(nums))


    p1 = 0
    for key in keys:
        for lock in locks:
            fit = all([a + b <= R-2 for a, b in zip(key, lock)])
            p1 += fit


    print(p1)
     # 2950

