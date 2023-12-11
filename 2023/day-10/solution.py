with open("2023\day-10\input.txt") as f: input = [[char for char in line] for line in f.read().splitlines()]

pos = None
for y, line in enumerate(input):
  if 'S' in line:
    pos = (y, line.index('S'))
    break
    
VALID_CONNECTIONS = {
  (-1, 0):  ['|', '7', 'F'], # top connections
  (0, 1): ['-', 'J', '7'], # right connections
  (1, 0): ['|', 'L', 'J'], # bottom connections
  (0, -1): ['-', 'L', 'F'], # left connections
}

VALID_DIRECTIONS = {
  '|': [(-1, 0), (1, 0)],
  '-': [(0, -1), (0, 1)],
  'L': [(-1, 0), (0, 1)],
  'J': [(-1, 0), (0, -1)],
  '7': [(0, -1), (1, 0)],
  'F': [(0, 1), (1, 0)],
  'S': [(-1, 0), (0, 1), (1, 0), (0, -1)]
}

queue = [pos] # Start with S
distance = 0
visited = []
while len(queue) > 1 or input[queue[0][0]][queue[0][1]] == 'S':
  y, x = queue.pop(0) # current pos
  current_pipe = input[y][x]
  visited.append((y, x))

  connected_pipes = []
  for direction in VALID_DIRECTIONS[current_pipe]:
    ny, nx = y + direction[0], x + direction[1]
    if not (0 <= nx < len(line) and 0 <= ny < len(input)): continue
    if (ny, nx) not in visited and input[ny][nx] in VALID_CONNECTIONS[direction]: queue.append((ny, nx))
  
  distance += 1

visited.append(queue[0])
print(distance//2)

# convert S into a pipe
u, r, d, l = False, False, False, False
for s_direction in VALID_DIRECTIONS['S']:
  ny, nx = pos[0] + s_direction[0], pos[1] + s_direction[1]
  if not (0 <= nx < len(line) and 0 <= ny < len(input)): continue
  if input[ny][nx] in VALID_CONNECTIONS[s_direction]:
    if s_direction == (-1, 0): u = True
    elif s_direction == (0, 1): r = True
    elif s_direction == (1, 0): d = True
    elif s_direction == (0, -1): l = True

if u and d: input[pos[0]][pos[1]] = '|'
if l and r: input[pos[0]][pos[1]] = '-'
if u and r: input[pos[0]][pos[1]] = 'L'
if u and l: input[pos[0]][pos[1]] = 'J'
if d and l: input[pos[0]][pos[1]] = '7'
if d and r: input[pos[0]][pos[1]] = 'F'

# Part 2
enclosed = 0
for y, line in enumerate(input):
  for x in range(len(line)):
    if not (y, x) in visited: 
      crossings = 0
      for step in range(x+1, len(line)):
        if not (y, step) in visited: continue
        if line[step] in ["|", "F", "7"]:
          crossings += 1
      enclosed += crossings % 2 == 1
      
print(enclosed)

# Your puzzle answer was 7102.
# Your puzzle answer was 363.