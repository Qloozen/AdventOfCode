import heapq

class Node():
  def __init__(self, heat, y, x):
    self.heat_dist = float('inf')
    self.prev = None
    self.heat = heat
    self.y = y
    self.x = x
    self.direction = (0, 0) 
    self.steps = 0
    

with open("ex.txt") as f:
  input = [[Node(int(char), y, x) for x, char in enumerate(line)] for y, line in enumerate(f.read().splitlines())]

def dijkstra(start_node):
  pq = [(start_node.heat, (start_node.y, start_node.x))]
  visited = set()

  while pq:
    heat, (y, x) = heapq.heappop(pq)
    if (y, x) in visited: continue

    visited.add((y, x))

    for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
      y2 = y + a
      x2 = x + b
      if not (0 <= y2 < len(input) and 0 <= x2 < len(input[0])): continue
      if (y2, x2) in visited: continue
      neighbor = input[y2][x2]

      # Doesn't work yet..
      #
      # if input[y][x].direction == (a, b): 
      #    if neighbor.steps > 3: 
      #       continue
      #    neighbor.steps = input[y][x].steps + 1
      # else:
      #    neighbor.steps +=1

      # neighbor.direction = (a, b)
      heat_dist = heat + neighbor.heat

      if heat_dist < neighbor.heat_dist:
        neighbor.heat_dist = heat_dist
        neighbor.prev = input[y][x]
        heapq.heappush(pq, (neighbor.heat_dist, (y2, x2)))

dijkstra(input[0][0])

print(input[-1][-1].heat)
print(input[-1][-1].heat_dist)

def print_path(grid, end):
    node = end
    while node:
        y, x = node.y, node.x
        grid[y][x] = f"{grid[y][x].heat}*"
        node = node.prev

    for row in grid:
        print(" ".join(map(lambda cell: cell if type(cell) is str else str(cell.heat) + " ", row)))


print_path(input, input[-1][-1])

