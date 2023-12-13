with open("2023\day-13\input.txt") as f: 
  input = [[[char for char in line] for line in pattern.splitlines()] for pattern in f.read().split("\n\n")]

def T(pattern): return list(zip(*pattern))

def reflection(pattern, part):
  mirror_index = 1
  while mirror_index < len(pattern):
    left, right = list(reversed(pattern[:mirror_index])), pattern[mirror_index:]
    similar = zip(left, right)

    if part == 1 and all(map(lambda pair: pair[0] == pair[1], similar)): return mirror_index
    elif part == 2:
      smuges = 0
      for line_pair in similar:
        for char_pair in zip(*line_pair):
          if char_pair[0] != char_pair[1]: smuges += 1

      if smuges == 1: return mirror_index

    mirror_index += 1
  return 0

def run(part):
  row_count, col_count = 0, 0

  for pattern in input:
    row_index = reflection(pattern, part)
    row_count += row_index

    if row_index > 0 : continue

    col_index = reflection(T(pattern), part)
    col_count += col_index

  print(100 * row_count + col_count)

for part in [1, 2]: run(part)

# 21520 too low

# Your puzzle answer was 33520.
# Your puzzle answer was 34824.