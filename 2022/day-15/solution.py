TARGET_Y = 2000000 # part1
MAX_Y = 4000000 # part2
with open("day-15/input.txt") as f:
    input = f.read().splitlines()
    objects = []
    all_objects = set()
    for line in input:
        sx = int(line.split('x=')[1].split(',')[0])
        sy = int(line.split('y=')[1].split(":")[0])
        bx = int(line.split('x=')[2].split(',')[0])
        by = int(line.split('y=')[2].split(":")[0])
        objects.append([(sy, sx), (by, bx)])
        all_objects.add((sy, sx))
        all_objects.add((by, bx))

# goes over all sensor/beacon pairs and find the coverage on the given Y in ranges
def find_ranges_on_line(target_y,) -> set:
    ranges = set()
    for pair in objects:
        sy, sx = pair[0] 
        by, bx = pair[1] 
        dist = abs(sx- bx) + abs(sy- by)
        top_index, bottom_index  = sy-dist, sy+dist 

        in_range = target_y >= top_index and target_y <= bottom_index
        
        if in_range:
            from_center = abs(sy-target_y)
            if from_center == 0:
                ranges.add((sx-dist, sx+dist))
            ranges.add((sx-(dist-from_center), sx+(dist-from_center)))
    return ranges

# returns total coverage on a line including all beancons/sensors on the line
# searches for a gap between ranges and terminates immediately after
def find_coverage_on_line(target_y) -> int:
    ranges = find_ranges_on_line(target_y)
    sorted_ranges = list(sorted(ranges, key=lambda x: x[0]))

    prev_highest = sorted_ranges[0][1]
    zipped_ranges = list(zip(sorted_ranges, sorted_ranges[1:]))
    for prev, curr in zipped_ranges:
        if curr[0] > prev_highest:
            gap_x = prev[1]+1
            # print(f"gap found at y={target_y}, x={gap_x}")
            print(gap_x * MAX_Y + target_y)
            exit(0)
        elif curr[1] > prev_highest:
            prev_highest = curr[1]

    lowest = sorted_ranges[0][0]
    higest = prev_highest
    return abs(lowest - higest)+1    

# part 1
coverage = find_coverage_on_line(TARGET_Y)
objects_on_line = len(list(filter(lambda obj: obj[0] == TARGET_Y, all_objects)))
print(coverage - objects_on_line)


# part 2 - change start to 0 for brute forcing
for y_index in range(3186981, MAX_Y):
    find_coverage_on_line(y_index)

# Your puzzle answer was 5256611
# Your puzzle answer was 13337919186981