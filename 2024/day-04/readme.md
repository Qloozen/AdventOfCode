## Part 1

> The goal is to find how many times the word `XMAS` occurs in the input file. It can be found horizontally, vertically, and diagonally. Overlapping and reverse words are allowed.

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

### Solution

1. I started with a basic loop to iterate on each letter of every line.

```python
count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
```

2. On each position i check if the next 4 letters form the word `XMAS` or the reverse `SAMX`.

```python
if j + 4 <= len(lines[i]):
    count += lines[i][j:j+4] in ["XMAS", "SAMX"]
```

same for vertical

```python
if i+3 < len(lines):
    count +=''.join([lines[i+x][j] for x in range(4)]) in ["XMAS", "SAMX"]
```

3. Finally i manually check the four diagonal directions. By stepping 4 times in each direction and checking if the word `XMAS` is formed.

```python
count += i+3 < len(lines) and j+3 < len(lines[i]) and ''.join([lines[i+x][j+x] for x in range(4)])  == "XMAS" # bottom right
count += i-3 >=0 and j-3 >=0 and ''.join([lines[i-x][j-x] for x in range(4)]) == "XMAS"  # top left
count += i+3 < len(lines) and j-3 >=0 and ''.join([lines[i+x][j-x] for x in range(4)]) == "XMAS" # bottom left
count += i-3 >= 0 and j+3 < len(lines[i]) and ''.join([lines[i-x][j+x] for x in range(4)]) == "XMAS" # top right
```

## Part 2

> The goal is to find two `MAS` in the shape of an X. The MAS can be in any direction, but they must be in the shape of an X. Like this:

```
M.S
.A.
M.S
```

### Solution

1. I tought it would be easy to focus on finding the letter 'A' and then check if the adjacent letters are 'M' and 'S'. So I basically used the same double loop as before but now to find the letter 'A'. I also added some checks to avoid out of bounds errors.

```python
 if lines[i][j] == 'A':
      if i-1 < 0 or j-1 < 0: continue
      if i+1 > len(lines)-1 or j+1 > len(lines[i])-1: continue
```

2. Then I put the adjacent letters in a list, one for top left, bottom right and one for top right, bottom left.

```python
lr = sorted([lines[i-1][j-1], lines[i+1][j+1]])
rl = sorted([lines[i-1][j+1], lines[i+1][j-1]])
```

3. Finally I check if both lists have the letters 'M' and 'S'.

```python
count += lr == ['M', 'S'] and rl == ['M', 'S']
```
