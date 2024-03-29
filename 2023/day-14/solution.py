from ast import literal_eval

with open("2023\day-14\input.txt") as f: 
  input = [[char for char in line] for line in f.read().splitlines()]

def T(grid, reverse=False):
    return [list(row) for row in list(zip(*reversed(grid)))] if reverse else [list(row) for row in list(zip(*grid))]
  
def move(grid):
  for x in range(len(grid[0])):
    top = 0
    for y in range(len(grid)):
      a = grid[y][x]
      if a == '.': continue
      if y == 0 or a == '#' or grid[y-1][x] in ['O', '#']:
        top = y+1
        continue
      grid[y][x] = '.'
      grid[top][x] = 'O'
      top += 1
  return grid

def calc_total_load(grid):
    total_load = 0

    for i, line in enumerate(grid):
      load = len(grid) - i
      total_load += sum(load for char in line if char == 'O')
    
    return total_load

print(calc_total_load(move(input)))

def cycle(input):
  input = move(input)
  for i in range(3):
    input = move(T(reversed(input)))  # left, bottom, right

  input = T(reversed(input)) # transpose to original
  return input

seen = [str(input)]
last = 0
while True:
  last += 1
  input = cycle(input)
  if str(input) in seen: break
  seen.append(str(input))

first = seen.index(str(input))

target_index = (1000000000 - first) % (last - first) + first
print(calc_total_load(literal_eval(seen[target_index])))

# Your puzzle answer was 110090.
# Your puzzle answer was 95254.










  