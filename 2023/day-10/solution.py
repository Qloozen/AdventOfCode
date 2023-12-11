with open("2023\day-10\input.txt") as f: input = [line for line in f.read().splitlines()]

pos = None
for i, line in enumerate(input):
  if 'S' in line:
    pos = (i, line.index('S'))
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

print(distance//2)