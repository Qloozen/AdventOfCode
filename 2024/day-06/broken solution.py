import copy

with open("input.txt") as f:

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    lines = f.read().splitlines()
    C = len(lines[0])
    R = len(lines)
    pos = next(((i, line.index('^')) for i, line in enumerate(lines) if '^' in line), (0, 0))
    INITIAL = pos
    d = 0
    seen = {0: {pos}, 1: set(), 2: set(), 3: set()}


    def loop(pos, d, seen): # part 2 - doesn't give the right ans for the actual input
      while True:
        ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
        
        if not (0 <= ny < R and 0 <= nx < C): return False
        
        if lines[ny][nx] != '#':
          pos = (ny, nx)
          if pos in seen[d]: return True;
          seen[d].add(pos)
        else: 
          d = (d + 1) % 4
       

    loop_counter = 0
    blocks = []
    while True:
        ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
        
        if not (0 <= ny < R and 0 <= nx < C): 
            break
        
        if lines[ny][nx] != '#':
          is_loop = loop((pos[0], pos[1]), (d + 1) % 4, copy.deepcopy(seen))
          if is_loop: # part 2
             blocks.append((ny, nx))
             loop_counter += 1
          pos = (ny, nx)
          seen[d].add(pos)
        else: 
          d = (d + 1) % 4
     
    print(len(seen[0] | seen[1] | seen[2] | seen[3]))      
    print(len(set(blocks)))

        
            
# Your puzzle answer was 5404

# not 2216
# not 2221





    
    