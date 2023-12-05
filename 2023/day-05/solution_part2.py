import re
with open("2023/day-05/input.txt") as f:
  input = f.read().split("\n\n")
  seeds = list(map(int, re.findall(r"\d+", input[0])))
  almanac = []
  for i in range(1, len(input)):
    a_map = [list(map(int, re.findall(r"\d+", row))) for row in input[i].splitlines()[1:]]
    almanac.append(a_map)

src_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
# [(79, 92), (55, 67)] initial seed ranges

for a_map in almanac:
  dest_ranges = []
  while len(src_ranges) >= 1:
    src_s, src_e = src_ranges.pop()

    is_mapped = False

    for map_range in a_map:
      drs, srs, le = map_range # destination range start, source range start, length
      overlap_s = max(src_s, srs)
      overlap_e = min(src_e, srs + le - 1)
     
      if overlap_s <= overlap_e: # there is overlap -> map the corresponding destination range
        is_mapped = True
        dest_s = drs + (overlap_s - srs)
        dest_e = drs + (overlap_e - srs) 
        dest_ranges.append((dest_s, dest_e))

        if src_s < overlap_s: # left-over left side -> recheck with other ranges in the current map
          src_ranges.append((src_s, overlap_s - 1))

        if src_e > overlap_e: # left-over right side -> recheck with other ranges in the current map
          src_ranges.append((overlap_e + 1, src_e))
        break

    if not is_mapped:     
      dest_ranges.append((src_s, src_e)) # these numbers are not mapped -> destination numbers are the same for the next map.
  src_ranges = dest_ranges # output of the current map is the input of the next map

# Print the lowest number from the lowest range
sorted_ranges = sorted(src_ranges, key=lambda x: x[0])
print(sorted_ranges[0][0])

# Your puzzle answer was 69841803.

