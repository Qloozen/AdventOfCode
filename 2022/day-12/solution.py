class Node:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist
    
s = Node(0, 0 ,0)

with open("day-12/input.txt") as f:
    grid = []
    for line in f.read().splitlines():
        row = []
        for char in line:
            if char == 'S':
                s = (len(grid), len(row))
            row.append(char)
        grid.append(row)