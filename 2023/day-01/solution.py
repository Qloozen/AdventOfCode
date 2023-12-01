import re
from functools import reduce

# appending the first and last character to each number to prevent replacing overlapping numbers
digits_mapping = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r","five": "f5e","six": "s6x","seven": "s7n","eight": "e8t","nine": "n9e"}

with open("2023/day-01/input.txt") as f:
    input = [line.lower() for line in f.read().splitlines()]

def extract_numbers(input):
    extracted_numbers = ["".join(re.findall(r'\d+', line)) for line in input]
    return [int(x[0] + x[-1]) for x in extracted_numbers if len(x) > 0]

# part 1
ans_1 = sum(extract_numbers(input))

# part 2
mapped = [reduce(lambda acc, map: acc.replace(map[0], map[1]), digits_mapping.items(), line) for line in input]
ans_2 = sum(extract_numbers(mapped))

print(ans_1)
print(ans_2)

# Your puzzle answer was 56108.
# Your puzzle answer was 55652.