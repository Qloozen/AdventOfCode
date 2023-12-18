import heapq
from collections import namedtuple

with open("input.txt") as f:
  input = [[int(char) for char in line] for line in f.read().splitlines()]

Node = namedtuple("Node", "heat_dist y x dy dx steps")

def dijkstra():
  pq = [Node(heat_dist=0, y=0, x=0, dy=0, dx=0, steps=0)] # heat_dist as priority
  visited = set()

  while pq:
    current_node = heapq.heappop(pq)
    if current_node[1:] in visited: continue
    if (current_node.y, current_node.x) == (len(input) - 1, len(input[0]) - 1): 
      return current_node

    visited.add(current_node[1:]) # heat_dist is ignored in visited

    if (current_node.y, current_node.x) == (0, 0) or current_node.steps >= 4:
      for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        y2 = current_node.y + dy
        x2 = current_node.x + dx
        if not (0 <= y2 < len(input) and 0 <= x2 < len(input[0])): continue
        if (current_node.dy, current_node.dx) == (-dy, -dx): continue
        if (current_node.dy, current_node.dx) == (dy, dx): continue

        neighbor = Node(heat_dist=current_node.heat_dist + input[y2][x2], y=y2, x=x2, dy=dy, dx=dx, steps=1)
        heapq.heappush(pq, neighbor)
        
    if (current_node.y, current_node.x) != (0, 0) and current_node.steps < 10:
      y2 = current_node.y + current_node.dy
      x2 = current_node.x + current_node.dx
      if not (0 <= y2 < len(input) and 0 <= x2 < len(input[0])): continue
      
      neighbor = Node(heat_dist=current_node.heat_dist + input[y2][x2], y=y2, x=x2, dy=current_node.dy, dx=current_node.dx, steps=current_node.steps + 1)
      heapq.heappush(pq, neighbor)


last_node = dijkstra()
print(last_node.heat_dist)

# too low 1036
# Your puzzle answer was 1227.

