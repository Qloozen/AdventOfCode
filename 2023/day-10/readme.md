## Part 1

Using a form of a queue, we start of with the 'S' pipe, appending its neighbors to the queue. We then pop the first element of the queue, and append its neighbors to the queue. We keep track of the pipes we have seen, and only append the neighbors that we have not seen before. We continue this process until we have seen all the pipes.

```python
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
```

Note that I use maps "VALID_DIRECTIONS" and "VALID_CONNECTIONS" to determine which directions are valid for each pipe, and which pipes can connect to that direction. like pipe '-' can only have pipes at direction left and right. And only pipes -, L, F can connect to the left of it and only pipes -, J, 7 can connect to the right of it. To prevent a whole bunch of if statements, I map each option with the corresponding valid directions and connections.

```python
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
```

## Part 2

So after thinking about solutions, I count the amount of crossings from each non-loop item to the left direction. Basically when an item is inside the loop the amount of crossings to the left (or right) is odd. When an item is outside the loop the amount of crossings to the left (or right) is even. This would be easy if every crossing would be with a | but considering corners like FJ and L7, these count only as one. So I only include |, F, 7 as crossing. After that I count all the odd crossings.

NB: S should be converted to a pipe aswell, which I forgot to do.

My solution is quite slow (2-3 min) for part 2, but it works.
