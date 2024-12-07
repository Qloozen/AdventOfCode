## Part 1

> The goal is to trace down a route in a 2D grid with obstacles. There is a starting position and starting direction. An obsticle (**#**) will block the path and the guard will turn 90 degrees to the right. Once the guard leaves the grid, we can count the number of distinct positions visited.

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

### Solution

1. Prepare some stuff first

```python
lines = list(map(list, f.read().splitlines()))
C = len(lines[0])
R = len(lines)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INIT_POS = next(((i, line.index('^')) for i, line in enumerate(lines) if '^' in line), (0, 0))

d = 0
pos = INIT_POS
seen = {pos}
```

Above contains the grid, the number of columns and rows, and the initial position. The `DIRECTIONS` constant is a list of tuples (Y, X) that can be used to move in a certain direction, eliminating the need to write a bunch of if statements. The list goes in the order of up, right, down and left. The puzzle starts with the guard facing up, so the initial direction (`d`) is 0. The set `seen` will store all the visited positions.

2. Walk the guard until it leaves the grid

```python
while True:
    ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
    if not (0 <= ny < R and 0 <= nx < C): break

    if lines[ny][nx] != '#':
      pos = (ny, nx)
      seen.add(pos)
    else:
      d = (d + 1) % 4
```

Above code starts with getting the next position (`ny`, `nx`) based on the current position and direction. The line after checks if the next position is within the grid. If not, the loop breaks.

If the next position is not an obstacle, the guard moves to that position and adds it to the set of visited positions. Otherwise, the guard turns 90 degrees to the right.

**Finally** the result can be printed by getting the length of the set `seen`.

## Part 2

> The next goal is to force the guard to walk in a loop, but we can only place one obstacle at a time and not in the initial position. The goal is to find how many possible positions we can place the obstacle to force the guard to walk in a loop.

_My first solution of part 2 was broken, but worked with the example input. Here I tried to turn right at every step during the part 1 loop, checking if it would collide with a position that has been seen before (including the direction). This approach didn't work for my input, so I kinda brute forced it anyway._

### Solution

So I basically put an obstacle at every position the guard visited in part 1. For each 'new' version of the grid I ran almost the same code as in part 1, but now including the direction of visited steps. If the guard encounters a position in the same direction as before, it would mean he is walking in a loop.

```python
    def loop(pos, d):
      seen = set()

      while True:
        ny, nx = pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1]
        if not (0 <= ny < R and 0 <= nx < C): return False

        if lines[ny][nx] != '#':
          if (ny, nx, d) in seen: return True;
          pos = (ny, nx)
          seen.add((ny, nx, d))
        else:
          d = (d + 1) % 4

    counter = 0
    for y, x in seen:
       lines[y][x] = "#"
       counter += loop(INIT_POS, 0)
       lines[y][x]  = "."
```
