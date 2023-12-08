## Part 1

The goal is to go from node AAA to ZZZ using a sequence of instructions defined on the first line, which is **L**eft or **R**ight. Every node has two other nodes connected to it, one on the left and one on the right. You navigate the maze by following the instructions. From the input I defined a dictionary with all the nodes and their connections like this:

```python
{
  'AAA': (BBB, CCC),
  'BBB': (DDD, EEE),
  # ...
}
```

with a simple while loop you can follow the instructions until you find 'ZZZ'. (fyi: if the instructions end, you start over from the beginning)

```python
n = 'AAA'
distance = 0
while n != 'ZZZ':
  for instruction in instructions:
    if n == 'ZZZ': break
    distance += 1
    l, r = nodes[n]
    n = l if instruction == 'L' else r
print(distance)
```

## Part 2

Extending the code above to handle multiple starting points, including finding the steps where all starting nodes have found an end node at the same time is not viable. First I started defining the starting_nodes (every node ending with 'A'):

```python
starting_nodes = list(filter(lambda node: node.endswith('A'), nodes))
```

After that I keep track of the path (steps to nodes ending with Z) of every single starting node, the idea is the same as part 1 except that you have multiple starting points and multiple intermediate ending nodes:

```python
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
```

The goal is to find the amount of steps it takes for all starting nodes to reach an ending node at the same time. Since I noticed that there are not intermediate nodes ending with 'Z' I can just find the least common multiple of all the paths:

```python
z_distances = [path[0] for path in paths]

print(reduce(lcm, z_distances))
```
