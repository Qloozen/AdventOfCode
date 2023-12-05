import re
with open("2023/day-05/input.txt") as f:
  input = f.read().split("\n\n")
  seeds = list(map(int, re.findall(r"\d+", input[0])))
  almanac = []
  for i in range(1, len(input)):
    a_map = [list(map(int, re.findall(r"\d+", row))) for row in input[i].splitlines()[1:]]
    almanac.append(a_map)

source_numbers = seeds

# source_numbers = seeds
destination_numbers = []

for a_map in almanac:
  destination_numbers = source_numbers
  for num_i, num in enumerate(source_numbers):
    for map_range in a_map:
      d, s, l = map_range # destination range start, source range start, length
      if s <= num <= s + (l-1):
        offset = num - s
        source_destination = d + offset
        destination_numbers[num_i] = source_destination
        break
  source_numbers = destination_numbers      

print(min(destination_numbers))
# Your puzzle answer was 177942185.