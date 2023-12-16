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
      dir_y, dir_x = -dir_x, -dir_y
      visited.add((pos_y, pos_x, dir_y, dir_x))
      queue.append((pos_y, pos_x, dir_y, dir_x))

    elif next_char == "\\":
      dir_y, dir_x = dir_x, dir_y
      visited.add((pos_y, pos_x, dir_y, dir_x))
      queue.append((pos_y, pos_x, dir_y, dir_x))
    
    elif next_char in ["|", "-"]:
      crossed = [(0, 1), (0, -1)] if next_char == "|" else [(1, 0), (-1, 0)]
      if not (dir_y, dir_x) in crossed: continue

      beam_a = (pos_y, pos_x, dir_x, dir_y)
      beam_b = (pos_y, pos_x, -dir_x, -dir_y)

      for beam in [beam_a, beam_b]:
        if not beam in visited:
          visited.add(beam)
          queue.append(beam)
                  
  unique_positions = {(pos[0], pos[1]) for pos in visited}

  return len(unique_positions)

print(beam((0, -1, 0, 1)))


# Part 2
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