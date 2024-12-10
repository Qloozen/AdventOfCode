with open("input.txt") as f:
    input = []
    start_positions = []

    for i, line in enumerate(f.read().splitlines()):
        r = []
        for j, c in enumerate(line):
            r.append(int(c))
            if c == "0": start_positions.append((i, j))
        input.append(r)

    R = len(input)
    C = len(input)

    p1 = 0
    p2 = 0
    for s_pos in start_positions:
        q = [s_pos]
        score1 = 0
        score2 = 0
        end_trails = set() # part 1

        while len(q) > 0:
            pos = q.pop(0)

            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx = pos[0] + d[0], pos[1] + d[1]
                if not (0 <= ny < R and 0 <= nx < C) or input[ny][nx] - input[pos[0]][pos[1]] != 1: continue
                if input[ny][nx] == 9: 
                    score2 += 1 # part 2
                    if (ny, nx) not in end_trails: # part 1
                        score1 += 1
                        end_trails.add((ny, nx))
                q.append((ny, nx))
        p1 += score1
        p2 += score2
    print(p1)
    print(p2)

# Your puzzle answer was 719.
# Your puzzle answer was 1530.


