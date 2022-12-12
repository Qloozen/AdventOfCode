class Node:
    def __init__(self, row, col, step):
        self.row = row
        self.col = col
        self.step = step

    
starting_nodes = []

with open("day-12/input.txt") as f:
    grid = []
    for line in f.read().splitlines():
        row = []
        for char in line:
            if char == 'S':
                starting_nodes.insert(0, Node(len(grid), len(row), 0))
                row.append('a')
            elif char == 'a':
                starting_nodes.append(Node(len(grid), len(row), 0))
                row.append(char)
            else:
                row.append(char)
        grid.append(row)

def find_shortest_path(s):
    queue = [s]
    visited = set()
    visited.add((s.row, s.col))
    while len(queue) != 0:
        c = queue.pop(0)

        if grid[c.row][c.col] == "E":
            return c.step

        if (can_move(c.row, c.col-1, c, visited)): # left
            queue.append(Node(c.row, c.col-1, c.step+1))

        if (can_move(c.row, c.col+1, c, visited)): # right
            queue.append(Node(c.row, c.col+1, c.step+1))

        if (can_move(c.row-1, c.col, c, visited)): # up
            queue.append(Node(c.row-1, c.col, c.step+1))

        if (can_move(c.row+1, c.col, c, visited)): # down
            queue.append(Node(c.row+1, c.col, c.step+1))


def can_move(y, x, c, visited):
    if (x < 0 or x > len(grid[0])-1) or (y < 0 or y > len(grid)-1):
        return False
    if (ord(grid[y][x]) - ord(grid[c.row][c.col]) > 1):
        return False
    if (y, x) in visited:
        return False
    
    visited.add((y, x))
    return True


print(find_shortest_path(starting_nodes[0])) 
all_paths = [find_shortest_path(s) for s in starting_nodes]
print(min(filter(lambda x: x is not None, all_paths)))

# Your puzzle answer was 497
# Your puzzle answer was 492