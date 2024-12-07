with open("input.txt") as f:
    lines = list(map(list, f.read().splitlines()))
    C = len(lines[0])
    R = len(lines)
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    INIT_POS = next(((i, line.index('^')) for i, line in enumerate(lines) if '^' in line), (0, 0))
  
    d = 0
    pos = INIT_POS
    seen = {pos}

    # part 1
    while True:
        ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
        if not (0 <= ny < R and 0 <= nx < C): break
        
        if lines[ny][nx] != '#':
          pos = (ny, nx)
          seen.add(pos)
        else: 
          d = (d + 1) % 4
    
    print(len(seen))

    # part 2
    def loop(pos, d):
      seen = set()

      while True:
        ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]   
        if not (0 <= ny < R and 0 <= nx < C): return False
        
        if lines[ny][nx] != '#':
          if (ny, nx, d) in seen: return True;
          pos = (ny, nx)
          seen.add((ny, nx, d))
        else: 
          d = (d + 1) % 4

    counter = 0
    for y, x in seen:
       lines[y][x] = "#"
       counter += loop(INIT_POS, 0)
       lines[y][x]  = "."
       
          
    print(counter)
            
# Your puzzle answer was 5404
# Your puzzle answer was 1984





    
    