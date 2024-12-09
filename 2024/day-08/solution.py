from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()
    R = len(lines)
    C = len(lines[0])
    input = defaultdict(list)
    [input[c].append((i, j)) for i, line in enumerate(lines) for j, c in enumerate(line) if c != '.']

    antinodes = set()
    for antenna, coords in input.items():
        for pos1 in coords:
            for pos2 in coords:
                if pos1 == pos2: continue
                diff1 = (pos1[0] - pos2[0], pos1[1] - pos2[1])
                diff2 = (-diff1[0], -diff1[1])

                antinode1 = (pos1[0] + diff1[0], pos1[1] + diff1[1])
                antinode2 = (pos2[0] + diff2[0], pos2[1] + diff2[1])

                if 0 <= antinode1[0] < R and 0 <= antinode1[1] < C:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < R and 0 <= antinode2[1] < C:
                    antinodes.add(antinode2)
   
    print(len(antinodes))
    # Your puzzle answer was 269.
    
    # Optionally print out the grid with antinodes
    # for i, line in enumerate(lines):
    #     string = ""
    #     for j, c in enumerate(line):
    #         if c != '.': string += c
    #         elif (i, j) in antinodes: string += '#'
    #         else: string += '.'
    #     print(string)