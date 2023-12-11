## Part 1

The puzzle input is a grid of galaxies, where # = galaxy and . = empty space. The goal is to sum up the shortest distances between each galaxy pair. But there is a catch: each row or columns where there is only empty space, the empty space is expanded 2 times.

Initially I did this the lazy way of manually increasing the empty space in the input directly, it worked fine but in part 2 you needed to expand the empty spaces 100000 times. So I reworked my solution, to support part 1 and 2. I will explain the solution in part 2.

## Part 2

They provided use a nice overview of the empty rows and columns, that needed to be expanded. If you look at the first galaxy in line one (0, 3), the galaxy only passed one expansion point on the X axis, and 0 expansions points on the Y axis (since it's the first row). We then know the actual x value will be: x + x_points_passed \* (expansion_amount - 1). In part one the expansion amount is 2, which result in (0, 4):

```
   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
```

For each galaxy we calculate the actual x and y values, based on the amount of expansion points passed and the expansion amount.

```python
# indicies of expansion points
y_expansion_points = [i for i, line in enumerate(input) if all(char == "." for char in line)]
x_expansion_points = [i for i in range(len(input[0])) if all(line[i] == "." for line in input)]

galaxies = [] #coordinates of all galaxies (y, x)
for y, line in enumerate(input):
  for x, char in enumerate(line):
    if char == "#":
      # count how many expansion points we passed for each axis
      y_passed_points = sum(1 for ye in y_expansion_points if ye < y)
      x_passed_points = sum(1 for xe in x_expansion_points if xe < x)

      # calculate the actual x and y values, based on the expansion amount
      new_x = x + x_passed_points * (expansion_amount-1)
      new_y = y + y_passed_points * (expansion_amount-1)

      galaxies.append((new_y, new_x))
```

We can now create a list of all pairs. lets say we have galaxies [a, b, c, d]: **a** pairs with b, c, d, **b** pairs with c, d, **c** pairs with d. You can see we pair each galaxy with the ones that comes after it:

```python
  pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)-1) for j in range(i + 1, len(galaxies))]
```

In the end we simply get the absolute distance between each pair, and sum it up:

```python
total = sum(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in pairs)
```
