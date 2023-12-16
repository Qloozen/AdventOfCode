with open("input.txt") as f:
  input = [[char for char in line] for line in f.read().splitlines()]

def beam(pos):
  visited = set()
  queue = [pos]

  while queue:
      pos_y, pos_x, dir_y, dir_x = queue.pop(0)
      pos_y = pos_y + dir_y
      pos_x = pos_x + dir_x

      if not (0 <= pos_x < len(input[0]) and 0 <= pos_y < len(input)): continue

      next_char = input[pos_y][pos_x]
      
      if next_char == "." or (next_char == "-" and dir_y == 0) or (next_char == "|" and dir_x == 0):
        visited.add((pos_y, pos_x, dir_y, dir_x))
        queue.append((pos_y, pos_x, dir_y, dir_x))

      elif next_char == "/":
        if dir_y == 0 and dir_x == 1: dir_y, dir_x = -1, 0
        elif dir_y == 0 and dir_x == -1: dir_y, dir_x = 1, 0
        elif dir_y == -1 and dir_x == 0: dir_y, dir_x = 0, 1
        elif dir_y == 1 and dir_x == 0:  dir_y, dir_x = 0, -1

        visited.add((pos_y, pos_x, dir_y, dir_x))
        queue.append((pos_y, pos_x, dir_y, dir_x))

      elif next_char == "\\":
          if dir_y == 0 and dir_x == 1: dir_y, dir_x = 1, 0
          elif dir_y == 0 and dir_x == -1: dir_y, dir_x = -1, 0
          elif dir_y == -1 and dir_x == 0: dir_y, dir_x = 0, -1
          elif dir_y == 1 and dir_x == 0:  dir_y, dir_x = 0, 1
          visited.add((pos_y, pos_x, dir_y, dir_x))
          queue.append((pos_y, pos_x, dir_y, dir_x))

      elif next_char == "|": 
        if (dir_y, dir_x) in [(0, 1), (0, -1)]: 
          up = (pos_y, pos_x, -1, 0)
          down = (pos_y, pos_x, 1, 0)
          for x in [up, down]:
            if not x in visited:
              visited.add(x)
              queue.append(x)
      
      elif next_char == "-": 
        if (dir_y, dir_x) in [(1, 0), (-1, 0)]: 
          left = (pos_y, pos_x, 0, -1)
          right = (pos_y, pos_x, 0, 1)
          for x in [left, right]:
            if not x in visited:
              visited.add(x)
              queue.append(x)
                  
  unique_positions = {(pos[0], pos[1]) for pos in visited}

  return len(unique_positions)

print(beam((0, -1, 0, 1)))

values = []

for x in range(len(input[0])):
    values.append(beam((-1, x, 1, 0)))
    values.append(beam((len(input), x, -1, 0)))

for y in range(len(input)):
    values.append(beam((y, -1, 0, 1)))
    values.append(beam((y, len(input[0]), 0, -1)))
    
print(max(values))

# Your puzzle answer was 7951.
# Your puzzle answer was 8148.