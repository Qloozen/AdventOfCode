from functools import reduce
from math import lcm

with open("2023/day-08/input.txt") as f:
  instructions, _, *c = f.read().splitlines()
  nodes = {node: tuple(options[1:-1].split(", ")) for node, options in (line.split(" = ") for line in c)}

# Part 1
n = 'AAA'
distance = 0
while n != 'ZZZ':
  for instruction in instructions:
    if n == 'ZZZ': break
    distance += 1
    l, r = nodes[n]
    n = l if instruction == 'L' else r
print(distance)

# Part 2
starting_nodes = list(filter(lambda node: node.endswith('A'), nodes))

paths = []
for n in starting_nodes:
  path, z1, distance, finished_paths = [], None, 0, False

  while not finished_paths:
    for instruction in instructions:
      distance += 1
      l, r = nodes[n]
      n = l if instruction == 'L' else r

      if n.endswith('Z'):
        path.append(distance)
        distance = 0
        if n == z1:
          finished_paths = True
          break
        elif z1 == None: z1 = n
  paths.append(path)

z_distances = [path[0] for path in paths]

print(reduce(lcm, z_distances))


