ans = 0
ans2 = 0
with open("day-15/input.txt") as f:
    input = f.read().splitlines()
    data = []
    all_beacons = set()
    all_sensors = set()
    target_y=2000000
    for line in input:
        sx = int(line.split('x=')[1].split(',')[0])
        sy = int(line.split('y=')[1].split(":")[0])
        bx = int(line.split('x=')[2].split(',')[0])
        by = int(line.split('y=')[2].split(":")[0])
        data.append([(sy, sx), (by, bx)])
        if by == target_y:
            all_beacons.add((by, bx))
        if sy == target_y:
            all_sensors.add((sy, sx))

def find_detected(sensor, beacon, detected):
    sy, sx = sensor
    by, bx = beacon
    dist = abs(sx- bx) + abs(sy- by)

    top_index = sy-dist 
    bottom_index = sy+dist 

    in_range = target_y >= top_index and target_y <= bottom_index

    if in_range:
        steps = abs(sy-target_y)
        if steps == 0:
            detected.add((sx-dist, sx+dist))
        a = sx - (dist-steps)
        b = sx + (dist-steps)
        detected.add((a, b))

detected = set()

for line in data:
    sensor, beacon = line[0], line[1]
    find_detected(sensor, beacon, detected)


lowest = min(range[0] for range in detected)
higest = max(range[1] for range in detected)
    
objects = len(all_beacons) + len(all_sensors)

diff = abs(lowest - higest)+1
ans = diff - objects

print(ans)
