import sys
sys.setrecursionlimit(2000) 

with open("input.txt") as f:
    byte_list = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]
    R = 71
    C = 71

    # part 1
    def bfs(byte_list):
        start = (0, 0, 0)

        q = [start]
        seen = {(start[0], start[1])}
        while len(q) > 0:
            y, x, dist = q.pop(0)
            if y == R-1 and x == C-1:
                return dist

            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx = dy + y, dx + x
                if not (0 <= ny < R and 0 <= nx < C): continue
                if (nx, ny) in byte_list: continue
                neighbor = (ny, nx, dist + 1)
                if not (ny, nx) in seen and not neighbor in q:
                    q.append(neighbor)
                    seen.add((ny, nx))
        return None
    
    print(bfs(byte_list[:1024]))
    
    # part 2
    def dfs(pos, visited, byte_list):
        y, x = pos
        visited.add((y, x))
        if y == R-1 and x == C-1:
            return True
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = dy + y, dx + x
            if not (0 <= ny < R and 0 <= nx < C): continue
            if (ny, nx) in byte_list: continue
            if not (ny, nx) in visited:
               if dfs((ny, nx), visited, byte_list):
                   return True;
        return False
       

    low = 1025
    high = len(byte_list)

    result = -1
    while low <= high:
        mid = (low + high) // 2

        if not dfs((0, 0), set(), byte_list[:mid]):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    print(byte_list[result-1])

# Your puzzle answer was 438.
# Your puzzle answer was 26,22.


