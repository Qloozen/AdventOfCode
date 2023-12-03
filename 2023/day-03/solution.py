from collections import defaultdict 
from functools import reduce

with open("2023/day-03/input.txt") as f:
    input = [line.lower() for line in f.read().splitlines()]

SYMBOLS = set([char for line in input for char in line if not char.isdigit() and char != '.'])
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

digits = []
gear_parts = defaultdict(list) # part 2

for i, line in enumerate(input):
    digit = ""
    is_engine_part = False
    connected_gears = set() # part 2
    
    for j, char in enumerate(line):
        if char.isdigit():
            digit += char
            
            for x, y in DIRECTIONS:
                nx, ny = j + x, i + y
                if not (0 <= nx < len(line) and 0 <= ny < len(input)): continue
                if input[ny][nx] in SYMBOLS: is_engine_part = True
                if input[ny][nx] == '*': connected_gears.add((nx, ny)) # part 2

        if not char.isdigit() or j == len(line) - 1: 
            if is_engine_part:
                digits.append(int(digit))
            if connected_gears: # part 2
                for x, y in connected_gears: gear_parts[(x, y)].append(int(digit))
            is_engine_part = False
            connected_gears.clear() # part 2 
            digit = ""

print(sum(digits))

gear_ratio = reduce(lambda acc, parts: acc + (parts[0] * parts[1]) if len(parts) == 2 else acc, gear_parts.values(), 0)
print(gear_ratio)  

# Your puzzle answer was 546312.
# Your puzzle answer was 87449461.
