## Part 1

First I extracted the symbols from the input file, which are non-digits and not a dot (note that the example and the input have different symbols):

```python
SYMBOLS = set([char for line in input for char in line if not char.isdigit() and char != '.'])
```

After that I looped over all the characters of each line, keeping track of the current number by appending the digits to a string.

```python
digit = ""
for j, char in enumerate(line):
    if char.isdigit():
        digit += char
```

After reaching a new dot or the end of the line, the digit is checked if it is a engine part or not. After each digit the values are reset. At the end we sum all the engine parts.

FYI: a neat trick to check all adjacent characters in a grid is to store all the directions:

```python
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for x, y in DIRECTIONS:
  nx, ny = j + x, i + y # getting the adjacent coordinates
  if not (0 <= nx < len(line) and 0 <= ny < len(input)): continue # check if the coordinates are in the grid
  if input[ny][nx] in SYMBOLS: is_engine_part = True # do something in the adjacent coordinate
```

# Part 2

To find the gears that are connected to two part numbers, I added a dictionary with the (x, y) tuple of each gear. The dictionary might look like this:

```python
# gear coords: [part numbers]
{
    (0, 2): [123, 456],
    (10, 15): [123],
}
```

While finding the part numbers I keep track of all the connected gears, a `set()` is used to prevent duplicate gears for a single part number.

```python
connected_gears = set()
if input[ny][nx] == '*': connected_gears.add((nx, ny)) # add the gear coordinates to the set
```

After the part number is found and all connected gears are known, we add the part number to the corresponding gears in the dictionary.

```python
if connected_gears:
  for x, y in connected_gears: gear_parts[(x, y)].append(int(digit)) # add the gear coordinates to the set, NB: this is a defaultdict(list)
connected_gears.clear()
```

At last we can use the reduce function to get the gear ratio for all gears that have 2 connected part numbers.

```python
from functools import reduce
gear_ratio = reduce(lambda acc, parts: acc + (parts[0] * parts[1]) if len(parts) == 2 else acc, gear_parts.values(), 0)
```
